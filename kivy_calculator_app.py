from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window


Window.size = (310, 500)


class Calculator(App):

    def build(self):
        self.operators = ["/", "*", "+", "-"]
        self.last_was_operator = None
        self.last_button = None
        main_layout = BoxLayout(orientation='vertical', spacing=10, padding=20)

        self.solution = TextInput(multiline=False, readonly=True, halign="right", font_size=30)
        main_layout.add_widget(self.solution)

        buttons = [
            ['7', '8', '9', '/', '<-'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['.', '0', 'C', '+']
        ]
        for row in buttons:
            h_layout = BoxLayout(spacing=5)
            for label in row:
                btn = Button(text=label,
                             pos_hint={'center_x': 0.5, 'center_y': 0.5})
                btn.bind(on_press=self.on_button_press)
                h_layout.add_widget(btn)
            main_layout.add_widget(h_layout)

        equals = Button(text="=",
                        pos_hint={'center_x': 0.5, 'center_y': 0.5})
        equals.bind(on_press=self.on_solution)
        main_layout.add_widget(equals)

        return main_layout

    def on_button_press(self, instance):
        current = self.solution.text                              # This variable is of string type
        button = instance.text
        if button == 'C':
            # Clear the text from solution widget
            self.solution.text = ""
        elif button == '<-':
            # It will clear last character from solution widget
            self.solution.text = self.solution.text[:-1]
        # Here we are comparing self.last_was_operator as true and button in self.operators also as true
        elif self.last_was_operator and button in self.operators:
            # Don't add two operators right after the another
            return
        # or
        # elif self.last_was_operator == True and button in self.operators:
        #     # Don't add two operators right after the another
        #     return
        elif current == "" and button in self.operators:
            # First character can't be an operator
            return
        else:
            text = current + button
            self.solution.text = text
        self.last_button = button
        self.last_was_operator = self.last_button in self.operators      # This variable is boolean type

    def on_solution(self, instance):
        text = self.solution.text
        if text:
            solution = str(eval(text))
            self.solution.text = solution


if __name__ == '__main__':
    Calculator().run()