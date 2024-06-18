import kivy
import random

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

red = [1, 0, 0, 1]
green = [0, 1, 0, 1]
blue = [0, 0, 1, 1]
purple = [1, 0, 1, 1]

class HBoxLayoutExample(App):

    def build(self):
        layout = BoxLayout(orientation='vertical',
                           padding=40,
                           spacing=10)         
        colors = [red, green, blue, purple]

        for i in range(5):
            btn = Button(text=f"Bouton #{i+1}",
                        background_color=random.choice(colors))
            layout.add_widget(btn)

        return layout


class MainApp(App):

    def build(self):
        button = Button(
            text="Hello Kivy World",
            size_hint=(.5, .5),
            pos_hint={'center_x': .5, 'center_y': .5}
        )

        button.bind(on_press=self.on_press_button)

        return button 

    def on_press_button(self, instance):
        print('"Vous avez appuyez sur la touche"')




if __name__ == "__main__":
    #app = HBoxLayoutExample()
    app = MainApp()
    app.run()