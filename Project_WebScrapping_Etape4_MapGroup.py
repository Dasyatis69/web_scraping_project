import time
from selenium import webdriver
from selenium.webdriver.common.by import By # Utilisation du navigateur
from geopy.geocoders import Nominatim
import folium

COLOR=['red','blue', 'green', 'purple', 'orange', 'darkred','lightred', 'beige', 'darkblue', 'darkgreen', 'cadetblue', 'darkpurple','pink', 'lightblue', 'lightgreen', 'gray', 'black', 'lightgray']
companies = ['esme_sudria', 'ubisoft', 'simfactory']
addresses = ['40 RUE DU DOCTEUR ROUX 75015 PARIS', '2 AV PASTEUR 94160 SAINT-MANDE', '201 Avenue Daumesnil, Paris']
coordinate = []
listGroup=[0,1,2]

def PutMarkerOnMap(NomHotel,Coordinate,ListGroupe,ZOOM=11):
    center = [48.866667, 2.333333]
    geolocator = Nominatim(user_agent='Google Chrome')
    for address in addresses:
        _ = geolocator.geocode(address)
        coordinate.append((_.latitude, _.longitude))
    Map = folium.Map(location=center, zoom_start=ZOOM)
    for i in range (len(NomHotel)):
            folium.Marker(coordinate[i], popup=NomHotel[i], tooltip="Click To View More !",icon=folium.Icon(color=COLOR[ListGroupe[i]], icon_color="white", icon='header', prefix="fa")).add_to(Map)
    Map.show_in_browser()

PutMarkerOnMap(companies,addresses,listGroup)