import json
import matplotlib.pyplot as plt
from geopy.geocoders import Nominatim
import folium
from sklearn.cluster import KMeans


def load_json(json_file):
    return json.load(open(json_file))


def save_to_json(json_file, data):
    with open(json_file, "w") as write_file:
        json.dump(data, write_file, indent=4)


def get_hotel_list_with_location(json_file):
    dictionary = load_json(json_file)

    hotel_addresses = [dictionary['1'][str(i)] for i in range(30)]
    coordinate = []

    geolocator = Nominatim(user_agent="my_request")
    for address in hotel_addresses:
        coord = geolocator.geocode(address)
        coordinate.append((coord.latitude, coord.longitude) if coord is not None else coord)

    hotel_list = []
    for i in range(len(hotel_addresses)):
        if coordinate[i] is None:
            pass
        else:
            hotel_list.append([dictionary['0'][str(i)], 
                               float(dictionary['2'][str(i)]), 
                               coordinate[i][0], 
                               coordinate[i][1]
                               ])
    # for i in liste_hotel:
    #     print(i)
    return hotel_list


def get_X_from_hotel_list_with_location(hotel_list):
    return [[i[1], i[2], i[3]] for i in hotel_list]


def get_color_from_star_rating(star_rating):
    if star_rating >= 4.5:
        return 'green'
    elif 3.5 <= star_rating < 4.5:
        return 'blue'
    elif star_rating < 3.5:
        return 'red'


def map_in_browser_by_star_rating(hotel_list):
    hotel_map = folium.Map(location=[48.866667, 2.333333], zoom_start=13)
    geolocator = Nominatim(user_agent="my_request")
    for i in range(len(hotel_list)):
        folium.Marker(location=(hotel_list[i][2], hotel_list[i][3]),
                      icon=folium.Icon(color=get_color_from_star_rating(hotel_list[i][1])),
                      popup=hotel_list[i][0]
                      ).add_to(hotel_map)
    hotel_map.show_in_browser()
    return None


def map_in_browser_by_group(hotel_list, group_list, zoom=11):
    color = ['red', 'blue', 'green', 'purple', 'orange', 'darkred', 'lightred', 'beige', 'darkblue', 'darkgreen',
             'cadetblue', 'darkpurple', 'pink', 'lightblue', 'lightgreen', 'gray', 'black', 'lightgray']
    hotel_map = folium.Map(location=[48.866667, 2.333333], zoom_start=zoom)
    for i in range(len(hotel_list)):  # need i to match hotel_list[i] and group_list[i]
        folium.Marker(location=(hotel_list[i][2], hotel_list[i][3]),
                      popup=hotel_list[i][0],
                      tooltip="Click To View More !",
                      icon=folium.Icon(color=color[group_list[i]], 
                                       icon_color="white", 
                                       icon='header', 
                                       prefix="fa")
                      ).add_to(hotel_map)
    hotel_map.show_in_browser()
    return None


def test_nbr_cluster_kmeans(X):  # need to add normalization or standardisation of X to fit model
    inertia = list()
    nbr_of_cluster_to_test = [i+1 for i in range(10)]
    for i in nbr_of_cluster_to_test:
        km = KMeans(n_clusters=i, n_init='auto')  # raise warning messages if n_init isn't manually set to 'auto'
        km.fit(X)
        inertia.append(km.inertia_)
    plt.plot(nbr_of_cluster_to_test, inertia)
    plt.show()
    return None  # would be nice to return the nbr of cluster, but it would require function analysis


def get_prediction_from_kmeans(nbr_cluster, X):
    km = KMeans(n_clusters=nbr_cluster, n_init='auto')  # raise warning messages if n_init isn't manually set to 'auto'
    km.fit(X)
    return km.predict(X)


hotel_list = get_hotel_list_with_location("table_info_hotels.json")
map_in_browser_by_star_rating(hotel_list)
X = get_X_from_hotel_list_with_location(hotel_list)
save_to_json("X.json", X)
# test_nbr_cluster_kmeans(X)
hotel_group = get_prediction_from_kmeans(3, X)  # nbr_cluster=3 was deduced from test_nbr_cluster_kmeans(X)'s graph
map_in_browser_by_group(hotel_list, hotel_group)
