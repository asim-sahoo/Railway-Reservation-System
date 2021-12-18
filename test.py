# import module
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

div = soup.find_all("div", class_="namePart")
l = []
for i in div:
	
	try:
		j= ((i.text).split())
		x = "Train Code: ",j[0],"Train Details: ",j[1],j[2],j[3],j[4],j[5],j[6],j[7]
		l.append(x)
	except IndexError:
		pass
x = '\n'.join(map(lambda x: str(x[0]) + ' ' + str(x[1]) + ' ' + str(x[2]) + ' ' + str(x[3]) + ' ' + str(x[4]) + ' ' + str(x[5]) + ' ' + str(x[6]) + ' ' + str(x[7]), l))

print(x)
#print(y)
#print(l)



# for i in l:)
# 	print(i)
# def convertTuple(tup):
#         # initialize an empty string
#     str = ''
#     for item in tup:
#         str = str + item
#     return str
 
 
# # Driver code
# tuple = ('g', 'e', 'e', 'k', 's')
# str = convertTuple(tuple)
# print(str)



# div1 = soup.find_all("span", class_="Coach-Type")
# for i in div1:
# 	try:
# 		j= ((i.text).split())
# 		print(j)
# 	except IndexError:
# 		pass
# div2 = soup.find_all("span", class_="Ticket-Fair")
# for i in div2:
# 	try:
# 		j= ((i.text).split())
# 		print(j)
# 	except IndexError:
# 		pass
# print(div1)

