import folium
from geopy.geocoders import Nominatim

dict_hotels = {
    "hotel1": {"star_rating": 1, "address": "5 Rue Saint Roch, Paris"},
    "hotel2": {"star_rating": 3, "address": "36 rue George Sand, Paris"},
    "hotel3": {"star_rating": 5, "address": "201 Avenue Daumesnil, Paris"}
}
points = []
Paris = folium.Map(location=[48.866667, 2.333333], zoom_start=11)
geolocator = Nominatim(user_agent='Google Chrome')
for ad in dict_hotels:
    location = geolocator.geocode(dict_hotels[ad]["address"])
    points.append((location.latitude, location.longitude))
for i in range(len(points)):
    star_rating = dict_hotels[list(dict_hotels.keys())[i]]["star_rating"]
    if star_rating >= 4 and star_rating <= 5 :
        color = 'green'
    elif star_rating >= 2 and star_rating < 4 :
        color = 'blue'
    elif star_rating >= 0 and star_rating < 2 :
        color = 'red'
    folium.Marker(location = points[i],
                  icon=folium.Icon(color=color),
                  popup = list(dict_hotels.keys())[i]).add_to(Paris)
Paris.show_in_browser()