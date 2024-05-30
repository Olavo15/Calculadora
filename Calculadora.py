from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class CalculatorApp(App):
    def build(self):
        self.operators = ["/", "*", "+", "-"]
        self.last_was_operator = None
        self.last_button = None

        main_layout = BoxLayout(orientation="vertical")

        self.top_layout = TextInput(
            multiline=False,
            readonly=True,
            halign="right",
            font_size=55,
            background_color=(0.15, 0.15, 0.15, 1),
            foreground_color=(1, 1, 1, 1),
        )
        main_layout.add_widget(self.top_layout)

        self.solution = TextInput(
            multiline=False,
            readonly=True,
            halign="right",
            font_size=55,
            background_color=(0.1, 0.1, 0.1, 1),
            foreground_color=(1, 1, 1, 1),
        )
        main_layout.add_widget(self.solution)

        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            [".", "0", "C", "+"]
        ]
        button_colors = {
            "default": (0.2, 0.6, 0.86, 1),
            "operator": (0.2, 0.4, 0.6, 1),
            "clear": (1, 0.3, 0.3, 1),
            "equals": (0.3, 0.7, 0.3, 1)
        }

        for row in buttons:
            h_layout = BoxLayout()
            for label in row:
                if label in self.operators:
                    color = button_colors["operator"]
                elif label == "C":
                    color = button_colors["clear"]
                else:
                    color = button_colors["default"]
                
                button = Button(
                    text=label,
                    pos_hint={"center_x": 0.5},
                    background_normal='',
                    background_color=color,
                    color=(1, 1, 1, 1),
                    font_size=35,
                )
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            main_layout.add_widget(h_layout)

        equals_button = Button(
            text="=",
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            background_normal='',
            background_color=button_colors["equals"],
            color=(1, 1, 1, 1),
            font_size=35,
        )
        equals_button.bind(on_press=self.on_solution)
        main_layout.add_widget(equals_button)

        return main_layout

    def on_button_press(self, instance):
        current = self.solution.text
        button_text = instance.text

        if button_text == "C":
            self.solution.text = ""
            self.top_layout.text = ""
        elif button_text == "CE":
            self.solution.text = ""
        else:
            if current and (self.last_was_operator and button_text in self.operators):
                return
            elif current == "" and button_text in self.operators:
                return
            else:
                new_text = current + button_text
                self.solution.text = new_text
            self.last_button = button_text
            self.last_was_operator = self.last_button in self.operators

    def on_solution(self, instance):
        text = self.solution.text
        if text:
            try:
                solution = str(eval(self.solution.text))
                self.top_layout.text = self.solution.text + " ="
                self.solution.text = solution
            except Exception:
                self.top_layout.text = "Error"
                self.solution.text = ""


if __name__ == '__main__':
    CalculatorApp().run()
