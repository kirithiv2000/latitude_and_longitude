import requests,pprint,json
from bs4 import BeautifulSoup
from find_geolocation import find_geolocation


latlan=find_geolocation()
latlan=latlan.split(" ")
lat,lon="lat="+latlan[0][:-1:],"lon="+latlan[2][:-1:]
geocode="geocode?"+lat+"%20%20&"+lon
requestsurl="https://developers.zomato.com/api/v2.1/"
categories="categories"
geocodeurl=requestsurl+geocode
print(geocodeurl)
r = requests.get(geocodeurl, headers={"user_key": "a79201374373ff188cca7a39151e5cd8", "Accept": "application/json"})
r=json.loads(r.text)
pprint.pprint(r)






