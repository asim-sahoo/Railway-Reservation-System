from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.screen import MDScreen
from kivymd.uix.behaviors import FakeRectangularElevationBehavior
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.button import MDFloatingActionButton

sm = ScreenManager()

class UserName(FakeRectangularElevationBehavior, MDFloatLayout):
    pass

class Password(FakeRectangularElevationBehavior, MDFloatLayout):
    pass
class LoginScreen(MDScreen):
    pass

class LoginScreen1(MDScreen):
    pass

class LoginScreen2(MDScreen):
    pass

class LoginScreen3(MDScreen):
    pass

class MainScreenManager(ScreenManager):
    pass