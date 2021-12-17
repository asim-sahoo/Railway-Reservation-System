from kivymd.uix.dialog import MDDialog
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from database import DataBase
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.dialog import MDDialog
from kivymd.uix.screen import MDScreen
from kivymd.uix.behaviors import FakeRectangularElevationBehavior
from kivymd.uix.floatlayout import MDFloatLayout

class UserName(FakeRectangularElevationBehavior, MDFloatLayout):
    pass

class Password(FakeRectangularElevationBehavior, MDFloatLayout):
    pass
class LoginScreen(MDScreen):
    pass

class LoginScreen1(MDScreen):
    pass

class LoginScreen2(MDScreen):
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    def loginBtn(self):
        if db.validate(self.email.text, self.password.text):
            MainWindow.current = self.email.text
            self.reset()
            self.manager.current = "main"            
        else:
            invalidLogin()

    def reset(self):
        self.email.text = ""
        self.password.text = ""

class LoginScreen3(MDScreen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count("@") == 1 and self.email.text.count(".") > 0:
            if self.password.text != "":
                db.add_user(self.email.text, self.password.text, self.namee.text)
                self.reset()
                self.manager.current = "loginscreen2"
            else:
                invalidForm()
        else:
            invalidForm()

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""

class MainWindow(Screen):
    n = ObjectProperty(None)
    current = ""

    def on_enter(self, *args):
        password, name, created = db.get_user(self.current)
        self.n.text = "Hi, " + name
    
class MainScreenManager(ScreenManager):
    pass

def invalidLogin():
    d1 = MDDialog(title='Invalid Login',text='Invalid username or password.',radius=[20,20,20,20])                  
    d1.open()

def invalidForm():
    d2 = MDDialog(title='Invalid Form',text='Please fill in all inputs with valid information.',radius=[20,20,20,20])
    d2.open()

sm = MainScreenManager()
db = DataBase("users.txt")

# screens = [MainWindow(name="main"),LoginScreen(name="loginscreen"), LoginScreen1(name="loginscreen1"),LoginScreen2(name="loginscreen2"),LoginScreen3(name="loginscreen3")]
# for screen in screens:
#     sm.add_widget(screen)