# import requests
# import json
# url1 = "https://indianrailways.p.rapidapi.com/findstations.php"
# st1 = "kharagpur"
# querystring1 = {"station":st1}
# headers1 = {
#     'x-rapidapi-host': "indianrailways.p.rapidapi.com",
#     'x-rapidapi-key': "d1fb13fbb2msh6b11d47bc02c3aep17e760jsn49deee70a758"
#     }
# response = requests.request("GET", url1, headers=headers1, params=querystring1)
# i1 = response.__dict__['_content'].decode("utf-8")
# res1 = json.loads(i1)["stations"]
# print(res1)
from bs4 import BeautifulSoup
import requests
# def getdata(url):
#     r = requests.get(url)
#     return r.text
r=requests.get("https://www.travelkhana.com/rail-infoindian-railway-station-list-with-station-code/")

soup = BeautifulSoup(r.content, 'html.parser')
for s in soup.select('script'):
    s.extract()
# div = soup.find_all("table")
print(soup)