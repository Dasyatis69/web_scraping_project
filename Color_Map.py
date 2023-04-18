import folium
from geopy.geocoders import Nominatim

dict_hotels = {
    "hotel1": {"star_rating": 1, "address": "5 Rue Saint Roch, Paris"},
    "hotel2": {"star_rating": 3, "address": "36 rue George Sand, Paris"},
    "hotel3": {"star_rating": 5, "address": "201 Avenue Daumesnil, Paris"}
}
points = []
def PutMarkerOnMap(dict_hotel,zoom=11):
    Paris = folium.Map(location=[48.866667, 2.333333], zoom_start=zoom)
    geolocator = Nominatim(user_agent='Google Chrome')
    for ad in dict_hotels:
         location = geolocator.geocode(dict_hotels[ad]["address"])
         points.append((location.latitude, location.longitude))
    for i in range(len(dict_hotel)):
        star_rating = dict_hotels[list(dict_hotels.keys())[i]]["star_rating"]
        if star_rating >= 3.5 and star_rating <= 5 :
            color = 'green'
        elif star_rating >= 2 and star_rating < 3.5 :
            color = 'orange'
        elif star_rating >= 0 and star_rating < 2 :
            color = 'red'
        folium.Marker(location = points[i],icon=folium.Icon(color=color,icon_color="white",icon='header',prefix='fa'),popup = list(dict_hotels.keys())[i]).add_to(Paris)
    Paris.show_in_browser()

PutMarkerOnMap(dict_hotels)