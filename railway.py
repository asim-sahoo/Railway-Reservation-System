from kivy.core.text import LabelBase
from kivy.uix.behaviors import button
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.widget import Widget
from kivymd.app import MDApp
from kivy.app import App
from kivymd.uix.button import MDFloatingActionButton
from kivymd.uix.dialog import MDDialog
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Animation, Window
from kivy.uix.screenmanager import Screen
from kivymd.uix.button import MDFillRoundFlatButton, MDRaisedButton
from kivy.uix.image import Image
from kivymd.uix.behaviors import FakeRectangularElevationBehavior
from kivymd.uix.floatlayout import MDFloatLayout


Window.size = (1920,1080)

helper = """
ScreenManager:
    Home:
    Main:
    Login:
<Home>:
    name: "home"
    Image:
        source: "w3.gif"
        size_hint: 1, 1
        pos_hint: {"center_x": .5, "center_y": .5}
        anim_delay: 0.04
        anim_loop: 0
        allow_stretch: True
        keep_ratio: False
    MDCard:
        size_hint: (.4,.7)
        pos_hint: {"center_x": .5, "center_y": .5}
        md_bg_color: 1,1,1,1
        elevation: 20
        radius: [35,35,35,35]
        padding: 0
    
    Image:
        source: "train.png"
        size_hint: .26, .26
        pos_hint: {"center_x": .5, "center_y": .65}
    MDLabel:
        text: "RAILWAY RESERVATION SYSTEM"
        font_name: "TPoppins"
        font_size: "33sp"
        pos_hint: {"center_x": .5, "center_y": .45}
        halign: "center"
        color: rgba(0,0,0,255)
    MDLabel:
        text: "Book Tickets Easily"
        font_name: "SPoppins"
        font_size: "28sp"
        pos_hint: {"center_x": .5, "center_y": .4}
        halign: "center"
        color: rgba(0,0,0,255)
    MDFillRoundFlatButton:
        text :"PROCEED"
        pos_hint: {"center_x": 0.5, "center_y": 0.27}
        font_size: "20sp"
        size_hint: .20, .065
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
            source: "train.png"
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
        source: "bg5.png"
        size_hint: 1.1, 1.1
        pos_hint: {"center_x": .5, "center_y": .5}
    MDCard:
        size_hint: (.6,.85)
        pos_hint: {"center_x": .5, "center_y": .5}
        md_bg_color: 1,1,1,1
        elevation: 20
        radius: [35,35,35,35]
        #Image:
            #source: "train.png"
            #size_hint: .9, .9
            #pos_hint: {"center_x": .05, "center_y": .5}
    UserName:
        size_hint: .25,.09
        pos_hint: {"center_x": .35, "center_y": .55}
        md_bg_color: 1,1,1,1
        elevation: 17
        radius: [15]
        Image:
            source: "user.png"
            size_hint: .4,.4
            pos_hint: {"center_x": .9, "center_y": .48}
        TextInput:
            hint_text: "Username"
            size_hint: .8, None
            pos_hint: {"center_x": .41, "center_y": .41}
            height: self.minimum_height
            cursor_color: 0,0,0,1
            cursor_width: "2sp"
            multiline: False
            background_color: 0,0,0,0
            padding: 15
            font_name: "SPoppins"
            font_size: "14sp"
            hint_text_color: rgba(3, 144, 252,255)
    Password:
        size_hint: .25,.09
        pos_hint: {"center_x": .35, "center_y": .43}
        md_bg_color: 1,1,1,1
        elevation: 17
        radius: [15]
        Image:
            source: "key.png"
            size_hint: .4,.4
            pos_hint: {"center_x": .9, "center_y": .48}
        TextInput:
            hint_text: "Password"
            size_hint: .78, None
            pos_hint: {"center_x": .41, "center_y": .41}
            height: self.minimum_height
            cursor_color: 0,0,0,1
            cursor_width: "2sp"
            multiline: False
            background_color: 0,0,0,0
            padding: 15
            font_name: "SPoppins"
            font_size: "14sp"
            hint_text_color: rgba(3, 144, 252,255)
    
"""

class UserName(FakeRectangularElevationBehavior, MDFloatLayout):
    pass

class Password(FakeRectangularElevationBehavior, MDFloatLayout):
    pass
class Home(Screen):
    pass

class Main(Screen):
    pass

class Login(Screen):
    pass

sm = ScreenManager()
sm.add_widget(Main(name='home'))
sm.add_widget(Main(name='main'))
sm.add_widget(Login(name='login'))
class Railway(MDApp):
    def show(self):
        #close = MDRaisedButton(text="OK", on_release=self.dialog_close)
        self.d = MDDialog(title="COVID 19 Alert:",text="\u2022 Passengers are advised to wear a mask, carry sanitizer, and follow social distancing norms\n\n\u2022 All Passenger to kindly note that on arrival at their destination, the traveling passengers will have to adhere to such health protocols as are prescribed by the destination State/UT.For other states, State Govt websites may be visited to ascertain the same.\n\n\u2022 No blanket and linen shall be provided in the train. Although Take Away Bedroll Kit is available in some trains on payment basis.",radius=[20,20,20,20])
        self.d.open()
    #def dialog_close(self, obj):
        #self.dialog.dismiss()
        #self.manager.current = 'main'    
    def build(self):
        screen = Builder.load_string(helper)
        return screen
    
if __name__ == "__main__":
    LabelBase.register(name="MPoppins", fn_regular="Poppins-Bold.ttf")
    LabelBase.register(name="BPoppins", fn_regular="Poppins-Medium.ttf")
    LabelBase.register(name="TPoppins", fn_regular="Poppins-Black.ttf")
    LabelBase.register(name="SPoppins", fn_regular="Poppins-Regular.ttf")
    Railway().run()