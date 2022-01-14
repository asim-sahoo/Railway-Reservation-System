from kivymd.uix.dialog import MDDialog
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from database import DataBase
from database1 import DataBase1
from database2 import DataBase2
from temp import Temp
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.dialog import MDDialog
from kivymd.uix.screen import MDScreen
from kivymd.uix.behaviors import FakeRectangularElevationBehavior
import requests
import json
import ast
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from bs4 import BeautifulSoup
from kivymd.uix.snackbar import Snackbar
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.list import OneLineListItem
import importlib

class LoginScreen(MDScreen):
    pass

class LoginScreen1(MDScreen):
    pass

class LoginScreen2(MDScreen):
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    def loginBtn(self):
        # if self.email.text != "" and self.password.text != "":
        #     if db.validate(self.email.text, self.password.text):
        #         MainWindow.current = self.email.text
        #         TwoChoice.current = self.email.text
        #         self.reset()
        #         self.manager.current = "choose"            
        #     else:
        #         invalidLogin()
        # else:
        #     invalidLogin()
        self.manager.current = "choose"

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
                signup()
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
    f_st = ObjectProperty(None)
    t_st = ObjectProperty(None)
    date = ObjectProperty(None)
    month = ObjectProperty(None)
    day = ObjectProperty(None)
    details = ObjectProperty(None)
    current = ""

    # def on_enter(self, *args):
    #     password, name, created = db.get_user(self.current)
    #     self.n.text = "Hi, " + name
    def check(self):
        url1 = "https://indianrailways.p.rapidapi.com/findstations.php"
        st1 = self.f_st.text
        querystring1 = {"station":st1}
        headers1 = {
            'x-rapidapi-host': "indianrailways.p.rapidapi.com",
            'x-rapidapi-key': "d1fb13fbb2msh6b11d47bc02c3aep17e760jsn49deee70a758"
            }
        response = requests.request("GET", url1, headers=headers1, params=querystring1)
        i1 = response.__dict__['_content'].decode("utf-8")
        res1 = json.loads(i1)["stations"]

        if len(res1)>1:
            invalidStation()
        else:
            for i1 in res1:
                s = st1
                if i1["stationName"] == s or s in i1["stationName"]:
                    n1 = i1["stationCode"]
            validStation()
    def check2(self):
        url2 = "https://indianrailways.p.rapidapi.com/findstations.php"
        st2 = self.t_st.text
        querystring2 = {"station":st2}
        headers2 = {
            'x-rapidapi-host': "indianrailways.p.rapidapi.com",
            'x-rapidapi-key': "d1fb13fbb2msh6b11d47bc02c3aep17e760jsn49deee70a758"
            }
        response = requests.request("GET", url2, headers=headers2, params=querystring2)
        i2 = response.__dict__['_content'].decode("utf-8")
        res2 = json.loads(i2)["stations"]
        
        if len(res2)>1:
            invalidStation()         
        else:
            for i2 in res2:
                s2 = st2
                if i2["stationName"] == s2 or s2 in i2["stationName"]:
                    n2 = i2["stationCode"]
            validStation()

    def Show(self):
        if self.f_st.text != "" and self.t_st.text != "" and self.date.text != "" and self.month.text != "" and self.day.text != "":
            try:  
                url1 = "https://indianrailways.p.rapidapi.com/findstations.php"
                st1 = self.f_st.text
                querystring1 = {"station":st1}
                headers1 = {
                    'x-rapidapi-host': "indianrailways.p.rapidapi.com",
                    'x-rapidapi-key': "d1fb13fbb2msh6b11d47bc02c3aep17e760jsn49deee70a758"
                    }
                response = requests.request("GET", url1, headers=headers1, params=querystring1)
                i1 = response.__dict__['_content'].decode("utf-8")
                res1 = json.loads(i1)["stations"]

                if len(res1)>1:
                    invalidStation()
                else:
                    for i1 in res1:
                        s = st1
                        if i1["stationName"] == s or s in i1["stationName"]:
                            n1 = i1["stationCode"]
                url2 = "https://indianrailways.p.rapidapi.com/findstations.php"
                st2 = self.t_st.text
                querystring2 = {"station":st2}
                headers2 = {
                    'x-rapidapi-host': "indianrailways.p.rapidapi.com",
                    'x-rapidapi-key': "d1fb13fbb2msh6b11d47bc02c3aep17e760jsn49deee70a758"
                    }
                response = requests.request("GET", url2, headers=headers2, params=querystring2)
                i2 = response.__dict__['_content'].decode("utf-8")
                res2 = json.loads(i2)["stations"]
                
                if len(res2)>1:
                    invalidStation()
                    
                else:
                    for i2 in res2:
                        s2 = st2
                        if i2["stationName"] == s2 or s2 in i2["stationName"]:
                            n2 = i2["stationCode"]
                def getdata(url):
                    r = requests.get(url)
                    return r.text
                date = self.date.text
                month = self.month.text
                day = self.day.text
                from_Station_code = n1
                from_Station_name = st1

                To_station_code = n2
                To_station_name = st2
                url = "https://www.railyatri.in/booking/trains-between-stations?from_code="+from_Station_code+"&from_name="+from_Station_name+"JN+&journey_date="+date+"+"+month+"+"+day+"&src=tbs&to_code="+To_station_code+"&to_name="+To_station_name+"+&user_id=-1639744636&user_token=41639744636&utm_source=dwebsearch_tbs_search_trains"

                htmldata = getdata(url)
                soup = BeautifulSoup(htmldata, 'html.parser')

                div = soup.find_all("div", class_="namePart")
    
                l = []
                for i in div:            
                    try:
                        j= (i.text)
                        l.append(j)
                    except IndexError:
                        pass
                

                def z(x):
                    z1 = x.text
                    db1.add_train(z1,date,month,n1,st1,n2,st2)
                    self.ids.details.clear_widgets()
                    self.manager.current = "main1"
                    print(z1)
                
                for i in l:
                    
                    self.ids.details.add_widget(OneLineListItem(text=i, on_press=z))
                               
                self.reset()
            except UnboundLocalError:
                notrain()
        else:
            invalidForm()
    

    def reset(self):
        self.f_st.text = ""
        self.t_st.text = ""
        self.date.text = ""
        self.month.text = ""
        self.day.text = ""

class Book(Screen):
    pnr=ObjectProperty(None)
    tx=ObjectProperty(None)
    fsn=ObjectProperty(None)
    tsn=ObjectProperty(None)
    dt_mon=ObjectProperty(None)
    passenger=ObjectProperty(None)
    fromhead= ObjectProperty(None)
    tohead=ObjectProperty(None)
    fromst= ObjectProperty(None)
    tost = ObjectProperty(None)
    def on_enter(self, *args):

        
        gg = dbt3.get_pass()
        print(gg)
        print(type(gg))
        pnr,tx,dt,mon,fsc,fsn,tsc,tsn,p = gg[0],gg[1],gg[2],gg[3],gg[4],gg[5],gg[6],gg[7],gg[8]
        gg1 = [gg[0],gg[1],gg[2],gg[3],gg[4],gg[5],gg[6],gg[7]]
        i=0
        while i<len(p):
            self.passenger.text += p[i]+' - '+p[i+1]+"\n"
            i+=2

        self.pnr.text="PNR: "+gg[0]
        self.tx.text="TRAIN: "+gg[1].strip()
        self.fsn.text="FROM: "+gg[5]
        self.tsn.text="TO: "+gg[7]
        self.dt_mon.text="DATE: "+gg[2]+" "+gg[3]
        self.fromhead.text=gg[4]
        self.tohead.text=gg[6]
        self.fromst.text=gg[5]
        self.tost.text=gg[7]
class TwoChoice(Screen):
    n = ObjectProperty(None)
    current = ""

    # def on_enter(self, *args):
    #     password, name, created = db.get_user(self.current)
    #     self.n.text = "Hi, " + name
        
class PnrCheck(Screen):
    pnrinputa = ObjectProperty(None)
    pnra= ObjectProperty(None)
    txa=ObjectProperty(None)
    fsna=ObjectProperty(None)
    tsna= ObjectProperty(None)
    dt_mona= ObjectProperty(None)
    passengera= ObjectProperty(None)
    
    
    def search(self):
        import database2
        importlib.reload(database2)
        from database2 import DataBase2
        db2a = DataBase2("MainDatabase.txt")
        if db2a.validate(self.pnrinputa.text):
                
                self.passengera.text = "PASSENGER: "
                current = self.pnrinputa.text
                pnr,tx,dt,mon,fsc,fsn,tsc,tsn,passenger = db2.get_pnr(current)
                
                passenger = ast.literal_eval(passenger)
                
                self.pnra.text="PNR: "+pnr
                self.txa.text="TRAIN: "+tx.strip()
                self.fsna.text="FROM: "+fsn
                self.tsna.text="TO: "+tsn
                self.dt_mona.text="DATE: "+dt+" "+mon
                i=0
                while i<len(passenger):
                    self.passengera.text += passenger[i]+' - '+passenger[i+1]+"\n"
                    i+=2
        else:
            norecord()

    def cancel(self):
        a_file = open("MainDatabase.txt", "r")
        a_file.seek(0,0)
        lines = a_file.readlines()
        a_file.close()
        for i in lines:
            
            if i[0:4] == self.pnrinputa.text:
                lines.remove(i)    
        new_file = open("MainDatabase.txt", "w+")

        for line in lines:
            new_file.write(line)

        new_file.close()
        self.pnra.text=""
        self.txa.text=""
        self.fsna.text=""
        self.tsna.text=""
        self.dt_mona.text=""
        self.passengera.text=""
        
class MainWindow1(Screen):
    na = ObjectProperty(None)
    p_n = ObjectProperty(None)
    p_a = ObjectProperty(None)
    passenger = []
    

    def on_enter(self, *args):
        he = db1.get_train()
        self.na.text = he

    def add_p(self):
        if self.p_n.text != "" and self.p_a.text != "":
            pa_n = self.p_n.text
            pa_a = self.p_a.text
            self.passenger.append(pa_n)
            self.passenger.append(pa_a)
            products_container = self.ids.passenger
            details = BoxLayout(size_hint_y=None,height=30,pos_hint={'top': 1})
            products_container.add_widget(details)

            name = Label(text=pa_n,size_hint_x=.2,color=(.06,.45,.45,1))
            age = Label(text=pa_a,size_hint_x=.3,color=(.06,.45,.45,1))
            details.add_widget(name)
            details.add_widget(age)
            self.reset()
        else:
            invalidForm()
        Payment.current = self.passenger
    def reset(self):
        self.p_n.text = ""
        self.p_a.text = ""

class Payment(Screen):
    file=open("MainDatabase.txt",'r')
    pnr=str(len(file.readlines())+8769)
    file.close()
    current = ""
    def bookbtn(self):
        ab = db1.get_data()
        tx,dt,mon,fsc,fsn,tsc,tsn=ab[0],ab[1],ab[2],ab[3],ab[4],ab[5],ab[6]
        db2.add_details(self.pnr,tx,dt,mon,fsc,fsn,tsc,tsn,self.current)
        dbt3.add_details(self.pnr,tx,dt,mon,fsc,fsn,tsc,tsn,self.current)
        self.manager.current = "bk"
class MainScreenManager(ScreenManager):
    pass


def invalidLogin():
    d1 = MDDialog(title='Invalid Login',text='Invalid username or password.',radius=[20,20,20,20])                  
    d1.open()

def invalidForm():
    d2 = MDDialog(title='Invalid Form',text='Please fill in all inputs with valid information.',radius=[20,20,20,20])
    d2.open()
def norecord():
    d2 = MDDialog(text='No Record Found',radius=[20,20,20,20])
    d2.open()
def notrain():
    d2 = MDDialog(title='Oops!',text='Something went wrong.It may cause due to following errors:\n\u2022Wrong Station names.Try Again!\n\u2022No Trains Found.',radius=[20,20,20,20])
    d2.open()
def invalidStation():
    Snackbar(
    text="Invalid Station! Try Again..",
    snackbar_x="5dp",
    snackbar_y="10dp",
    ).open()
def signup():
    d2 = MDDialog(text='Signed Up Successfully.',radius=[20,20,20,20])
    d2.open()
def validStation():
    Snackbar(
    text="Valid Station!",
    snackbar_x="5dp",
    snackbar_y="10dp",
    ).open()


sm = MainScreenManager()
db = DataBase("users.txt")
db1 = DataBase1("train.txt")
db2 = DataBase2("MainDatabase.txt")
dbt3 = Temp("temp.txt")
