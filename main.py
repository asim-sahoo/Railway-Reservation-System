import os
from kivymd.app import MDApp
from kaki.app import App
from kivy.factory import Factory
from kivy.core.window import Animation, Window
from kivy.core.text import LabelBase
Window.size = (1920,1080)


# main app class for kaki app with kivymd modules
class LiveApp(MDApp, App):

    DEBUG = 1 # set this to 0 make live app not working

    # *.kv files to watch
    KV_FILES = {
        os.path.join(os.getcwd(), "screens/screenmanager.kv"),
        os.path.join(os.getcwd(), "screens/login_screen/loginscreen.kv"),
    }

    # class to watch from *.py files
    CLASSES = {
        "MainScreenManager": "screens.screenmanager",
        "LoginScreen": "screens.screenmanager",
    }

    # auto reload path
    AUTORELOADER_PATHS = [
        (".", {"recursive": True}),
    ]


    def build_app(self):

        return Factory.MainScreenManager()




# finally, run the app
if __name__ == "__main__":
    LabelBase.register(name="TPoppins", fn_regular="E:\\Railway-Reservation-System test\\screens\\Poppins-Black.ttf")
    LabelBase.register(name="SPoppins", fn_regular="E:\\Railway-Reservation-System test\\screens\\Poppins-Regular.ttf")
    LabelBase.register(name="BPoppins", fn_regular="E:\\Railway-Reservation-System test\\screens\\Poppins-Medium.ttf")
    LabelBase.register(name="MPoppins", fn_regular="E:\\Railway-Reservation-System test\\screens\\Poppins-Bold.ttf")
    LiveApp().run()