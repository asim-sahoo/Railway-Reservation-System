
import requests
import json
from bs4 import BeautifulSoup

cont1 = True
while cont1:
    url1 = "https://indianrailways.p.rapidapi.com/findstations.php"
    st1 = input("From Station Name: ").upper()
    querystring1 = {"station":st1}
    headers1 = {
        'x-rapidapi-host': "indianrailways.p.rapidapi.com",
        'x-rapidapi-key': "d1fb13fbb2msh6b11d47bc02c3aep17e760jsn49deee70a758"
        }
    response = requests.request("GET", url1, headers=headers1, params=querystring1)
    i1 = response.__dict__['_content'].decode("utf-8")
    res1 = json.loads(i1)["stations"]
    if len(res1)>1:
        print("Be Specific")
    else:
        for i1 in res1:
            s = st1
            if i1["stationName"] == s or s in i1["stationName"]:
                n1 = i1["stationCode"]
    cont1 = False

###############################

cont = True
while cont:
    url2 = "https://indianrailways.p.rapidapi.com/findstations.php"
    st2 = input("To Station Name: ").upper()
    querystring2 = {"station":st2}
    headers2 = {
        'x-rapidapi-host': "indianrailways.p.rapidapi.com",
        'x-rapidapi-key': "d1fb13fbb2msh6b11d47bc02c3aep17e760jsn49deee70a758"
        }
    response = requests.request("GET", url2, headers=headers2, params=querystring2)
    i2 = response.__dict__['_content'].decode("utf-8")
    res2 = json.loads(i2)["stations"]    
    if len(res2)>1:
        print("Be Specific")
    else:
        for i2 in res2:
            s2 = st2
            if i2["stationName"] == s2 or s2 in i2["stationName"]:
                n2 = i2["stationCode"]
        cont = False

def getdata(url):
    r = requests.get(url)
    return r.text

date = input("Date: ")
month = input("Month: ").title()
day = input("Day: ").title()
from_Station_code = n1
from_Station_name = st1
To_station_code = n2
To_station_name = st2
url = "https://www.railyatri.in/booking/trains-between-stations?from_code="+from_Station_code+"&from_name="+from_Station_name+"JN+&journey_date="+date+"+"+month+"+"+day+"&src=tbs&to_code="+To_station_code+"&to_name="+To_station_name+"+&user_id=-1639744636&user_token=41639744636&utm_source=dwebsearch_tbs_search_trains"
htmldata = getdata(url)
soup = BeautifulSoup(htmldata, 'html.parser')


from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.list import MDList
from kivymd.uix.list import OneLineIconListItem
from kivy.uix.scrollview import ScrollView


class DemoApp(MDApp):

    def build(self):
        screen = Screen()
        scroll = ScrollView()
        list_view = MDList()
        div = soup.find_all("div", class_="namePart")
        l = []
        for i in div:            
            try:
                j= (i.text)
                l.append(j)
            except IndexError:
                pass
        for i in l:
            items = OneLineIconListItem(text=str(i))
            list_view.add_widget(items)
        scroll.add_widget(list_view)
        screen.add_widget(scroll)
        return screen


DemoApp().run()