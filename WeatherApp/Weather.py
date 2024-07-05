import json
import requests

city = input("Enter the name of the city\n ")
url=f"http://api.weatherapi.com/v1/current.json?key=5b1e069dd6be423487c114056240507&q={city}"
r= requests.get(url)
# print(r.text)

wdic= json.loads(r.text)
print(wdic["current"]["temp_c"])
