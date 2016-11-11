import googlemaps
from datetime import datetime
import webbrowser


gmaps = googlemaps.Client(key='YOUR_API_KEY')

# Geocoding an address
#'CIUDAD DE MEXICO,AZCAPOTZALCO,ANTONIO VALERIANO No. 211,EL ARENAL,2980'
def geocode_dir(direction):
	geocode_result = gmaps.geocode(direction)
	lat = geocode_result[0]['geometry']['location']['lat']
	lng = geocode_result[0]['geometry']['location']['lng']
	locat = str(lat)+","+str(lng)
	return locat

def deco_location(location):
	coordenates = "19.434437,-99.159583"
	return coordenates

#https://www.google.com.mx/maps/dir/19.434437,-99.159583/19.4451495,-99.187968/
def road(location, destination):
	road_w = "https://www.google.com.mx/maps/dir/"+location+"/"+destination+"/"
	webbrowser.open(road_w)
	return road_w


