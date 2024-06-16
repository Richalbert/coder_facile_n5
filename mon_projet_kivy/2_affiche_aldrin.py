from kivy.app import App
from kivy.uix.image import Image

class MainApp(App):

    def build(self):
        image = Image(source='image\Aldrin_Apollo_11_original.jpeg')
        return image


if __name__ == "__main__":
    app = MainApp()
    app.run()