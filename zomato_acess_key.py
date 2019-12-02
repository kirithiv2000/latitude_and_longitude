import requests,pprint,json
from bs4 import BeautifulSoup
from find_geolocation import find_geolocation


latlan=find_geolocation()
latlan=latlan.split(" ")
lat,lon="lat="+latlan[0][:-1:],"lon="+latlan[2][:-1:]
geocode="geocode?"+lat+"&"+lon
requestsurl="https://developers.zomato.com/api/v2.1/"
categories="categories"
geocodeurl=requestsurl+geocode
print(geocodeurl)
r = requests.get(geocodeurl, headers={"user_key": "a79201374373ff188cca7a39151e5cd8", "Accept": "application/json"})
r=json.loads(r.text)
# pprint.pprint(r)
for restaurant in r["nearby_restaurants"]:
	print("Shop Name                : ",restaurant["restaurant"]["name"])
	print("Average cost of 2 person : ",restaurant["restaurant"]["average_cost_for_two"])
	print("Accepted Currency        : ",restaurant["restaurant"]["currency"])
	print("Available food           : ",restaurant["restaurant"]["cuisines"])
	print("Rating                   : ",restaurant["restaurant"]["user_rating"]["aggregate_rating"])
	print("Votes                    : ",restaurant["restaurant"]["user_rating"]["votes"])
	print("Menu url                 : ",restaurant["restaurant"]["menu_url"])
	print("Url                      : ",restaurant["restaurant"]["url"])
	print("Address                  : ",restaurant["restaurant"]["location"]["address"])
	for rating in restaurant["restaurant"]["user_rating"]:
		if rating=="rating_tool_tip":
			print("Reason of Rating         : ",restaurant["restaurant"]["user_rating"]["rating_tool_tip"])
	print("--------------------------------------------------------------------------------------")






