from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.graphics.context_instructions import Color
from kivy.core.window import Window
from kivy.graphics import Rectangle
from kivymd.toast.kivytoast.kivytoast import toast
from kivy.logger import Logger
KV="""
application_osn:
    orientation:"vertical"
    size_hint:(0.8,0.8)
    pos_hint:{"center_x":0.66,"center_y":0.5}
    Label:
        font_size:"30sp"
        
    Button:
        text:root.lr
        background_color:'red'
        size_hint:(0.6,0.3)
        on_press: root.red()

    Button:
        text:root.lg
        background_color:'green'
        size_hint:(0.6,0.3)
        on_press: root.green()

    Button:
        text:root.lb
        background_color:'blue'
        size_hint:(0.6,0.3)
        on_press: root.blue()

    Button:
        text:root.lm
        font_color:'white'
        background_color:'black'
        size_hint:(0.6,0.3)
        on_press:root.im()
"""
class application_osn(BoxLayout):
    from jnius import autoclass
    Locale = autoclass('java.util.Locale')
    lang = Locale.getDefault().getLanguage()
    lr,lg,lb,lm="Красный","Зелёный","Синий","Моя картинка"
    match lang:
        case "de":lr,lg,lb,lm="Rot","Grün","Blau","Mein Bild"
        case "en":lr,lg,lb,lm="Red","Green","Blue","My picture"
    data_label = StringProperty("!")
    def red(self):
        Logger.info(self.lr)
        toast(self.lr)
        with self.canvas.before:
            self.bg = Color(rgba=(1,0,0,1))
            self.bg = Rectangle( pos=(0,0), size=Window.size)
    def green(self):
        Logger.info(self.lg)
        toast(self.lg)
        with self.canvas.before:
            self.bg = Color(rgba=(0,1,0,1))
            self.bg = Rectangle( pos=(0,0), size=Window.size)
    def blue(self):
        Logger.info(self.lb)
        toast(self.lb)
        with self.canvas.before:
            self.bg = Color(rgba=(0,0,1,1))
            self.bg = Rectangle( pos=(0,0), size=Window.size)
    def im(self):
        Logger.info(self.lm)
        toast(self.lm)
        with self.canvas.before:
            self.bg=Color(rgba=(1,1,1,1))
            self.bg = Rectangle(source='texture.png', pos=(0,0), size=Window.size)

class app(MDApp):
    running=True
    def build(self):
        return Builder.load_string(KV)
    def on_stop(self):
        self.running=False

if __name__ == "__main__":
    app().run()