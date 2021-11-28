from kivy.core.text import LabelBase
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.widget import Widget
from kivymd.app import MDApp
from kivy.app import App
from kivymd.uix.dialog import MDDialog
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen
from kivymd.uix.button import MDFillRoundFlatButton
from kivy.uix.image import Image

Window.size = (1920,1080)

helper = """
ScreenManager:
    Home:
    Main:
    Login:
<Home>:
    name: "home"
    Image:
        source: "bg5.png"
        size_hint: 1.1, 1.1
        pos_hint: {"center_x": .5, "center_y": .5}
    MDFillRoundFlatButton:
        text :"PROCEED"
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        font_size: "20sp"
        size_hint: .28, .065
        font_name: "BPoppins"
        on_press: root.manager.current = 'main'
<Main>:
    
    name: "main" 
    on_enter: app.show()
    Image:
        source: "bg5.png"
        size_hint: 1.1, 1.1
        pos_hint: {"center_x": .5, "center_y": .5}
    
    MDCard:
        size_hint: (.4,.8)
        pos_hint: {"center_x": .27, "center_y": .5}
        md_bg_color: 1,1,1,1
        elevation: 20
        radius: [40,40,40,40]
        Image:
            source: "D:\dtrain.png"
            size_hint: .26, .26
            pos_hint: {"center_x": .5, "center_y": .73}
           
    MDLabel:
        text: "Railway Reservation"
        font_name: "BPoppins"
        font_size: "40sp"
        pos_hint: {"center_x": .27, "center_y": .495}
        halign: "center"
        color: rgba(0,0,0,255)
    MDLabel:
        text: "System"
        font_name: "BPoppins"
        font_size: "40sp"
        pos_hint: {"center_x": .27, "center_y": .43}
        halign: "center"
        color: rgba(0,0,0,255)
    MDFillRoundFlatButton:
        text :"LOGIN"
        pos_hint: {"center_x": 0.27, "center_y": 0.33}
        font_size: "20sp"
        size_hint: .28, .065
        font_name: "BPoppins"
        on_press: root.manager.current = 'login'
    MDRoundFlatButton:
        text :"SIGN UP"
        pos_hint: {"center_x": 0.27, "center_y": 0.25}
        font_size: "20sp"
        size_hint: .28, .065
        font_name: "BPoppins"

<Login>:
    name: "login"
    Image:
        source: "bg4.png"
        size_hint: 1.1, 1.1
        pos_hint: {"center_x": .5, "center_y": .5}
    MDCard:
        size_hint: (.6,.85)
        pos_hint: {"center_x": .5, "center_y": .5}
        md_bg_color: 1,1,1,1
        elevation: 20
        radius: [35,35,35,35]
        padding: 0
        #Image:
            #source: "lbg.jpg"
            #size_hint: .9, .9
            #pos_hint: {"center_x": .05, "center_y": .5}
    
    
"""
class Home(Screen):
    pass

class Main(Screen):
    pass

class Login(Screen):
    pass

sm = ScreenManager()
sm.add_widget(Main(name='main'))
sm.add_widget(Login(name='login'))
class Railway(MDApp):
    def show(self):
        d = MDDialog(text="Hello")
        d.open()    
    def build(self):

        screen = Builder.load_string(helper)
        return screen
    

if __name__ == "__main__":
    LabelBase.register(name="MPoppins", fn_regular="Poppins-Bold.ttf")
    LabelBase.register(name="BPoppins", fn_regular="Poppins-Medium.ttf")
    Railway().run()