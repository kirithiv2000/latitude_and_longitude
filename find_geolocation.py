import requests,json
from bs4 import BeautifulSoup
def find_geolocation():

	google="https://google.com/"
	searchquery="search?q="
	our_query=input(">>> ENTER (place ) : ")
	global place
	place=our_query
	our_query="latitude and longitude of "+our_query.strip()
	end_="&oq=la&aqs=chrome.0.69i59l3j69i61l2j69i60.5204j0j7&sourceid=chrome&ie=UTF-8"
	our_query=our_query.replace(" ","+")
	URL=google+searchquery+our_query+end_
	r=requests.get(URL)

	soup=BeautifulSoup(r.text,"lxml")


	lat_lan=soup.find("div", class_="BNeawe iBp4i AP7Wnd").text
	place=soup.find("span", class_="BNeawe tAd8D AP7Wnd").text
	print("Latitude and longitude of {0} is {1}".format(place,lat_lan))
	return lat_lan,place
