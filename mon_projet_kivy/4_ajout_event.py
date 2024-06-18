import kivy

from kivy.app import App
from kivy.uix.button import Button



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
 
    app = MainApp()
    app.run()