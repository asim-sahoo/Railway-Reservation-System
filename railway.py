from kivy.core.text import LabelBase
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.widget import Widget
from kivymd.app import MDApp
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen
from kivymd.uix.button import MDFillRoundFlatButton
from kivy.uix.image import Image
Window.size = (1920,1080)
helper = """
ScreenManager:
    Main:
    Login:

<Main>:
    name: "main"
    MDFloatLayout:
        md_bg_color: 255/255,98/255,67/255,1
    MDCard:
        size_hint: (.4,.8)
        pos_hint: {"center_x": .5, "center_y": .5}
        md_bg_color: 189/255,219/255,255/255,1
        elevation: 13
        radius: [20,20,20,20]
        Image:
            source: "D:\dtrain.png"
            size_hint: .26, .26
            pos_hint: {"center_x": .5, "center_y": .7}
            canvas.before:
                Color:
                    rgb: 1,1,1,1

                Ellipse:
                    size: 267, 267
                    pos: 635, 377
    MDLabel:
        text: "Railway Reservation"
        font_name: "BPoppins"
        font_size: "35sp"
        pos_hint: {"center_y": .43}
        halign: "center"
        color: rgba(0,0,0,255)
    MDLabel:
        text: "System"
        font_name: "BPoppins"
        font_size: "35sp"
        pos_hint: {"center_y": .38}
        halign: "center"
        color: rgba(0,0,0,255)
    MDFillRoundFlatButton:
        text :"LOGIN"
        pos_hint: {"center_x": 0.5, "center_y": 0.3}
        font_size: "20sp"
        size_hint: .075, .065
        font_name: "BPoppins"



"""
class Main(Screen):
    pass
class Login(Screen):
    pass

sm = ScreenManager()
sm.add_widget(Main(name='main'))
sm.add_widget(Login(name='login'))
class Railway(MDApp):
        
    def build(self):

        screen = Builder.load_string(helper)
        
        return screen
    


if __name__ == "__main__":
    LabelBase.register(name="MPoppins", fn_regular="D:\\Poppins\\Poppins-SemiBold.ttf")
    LabelBase.register(name="BPoppins", fn_regular="D:\\Poppins\\Poppins-Medium.ttf")
    Railway().run()