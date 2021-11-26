from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivymd.uix.button import MDFillRoundFlatButton
from kivy.lang import Builder
from kivy.uix.image import Image
image = """

Image:
    source: "E:\py\Class 12\Railway-Reservation-System\Fp1.jpg"
    pos_hint: {"center_x": 0.1, "center_y": .5}
    size_hint: 1,1
"""
user = """
MDTextField:
    hint_text: "Enter username"
    icon_right_color: app.theme_cls.primary_color
    pos_hint:{'center_x': 0.6, 'center_y': 0.6}
    size_hint_x:None
    width:300
"""
passw = """
MDTextField:
    hint_text: "Enter Password"
    icon_right_color: app.theme_cls.primary_color
    pos_hint:{'center_x': 0.6, 'center_y': 0.5}
    size_hint_x:None
    width:300

"""
class RailwayApp(MDApp):
        
    
    def build(self):
        images = Builder.load_string(image)
        username = Builder.load_string(user)
        passwd = Builder.load_string(passw)
        screen = Screen()
        screen.add_widget(
            MDFillRoundFlatButton(
                text="Login",
                pos_hint={"center_x": 0.459, "center_y": 0.4},
            )
        )
        screen.add_widget(images)
        screen.add_widget(username)
        screen.add_widget(passwd)
        return screen

RailwayApp().run()