import requests
import json
from bs4 import BeautifulSoup

# URL de la page à scraper
url = "https://www.booking.com/searchresults.fr.html?label=gen173nr-1FCAEoggI46AdIM1gEaKoBiAEBmAEwuAEHyAEM2AED6AEB-AELiAIBqAIDuALh7Kr9BcACAQ&sid=e873717e28a36d85aa78da24dafe7f48&tmpl=searchresults&checkin_month=4&checkin_monthday=16&checkin_year=2023&checkout_month=4&checkout_monthday=17&checkout_year=2023&city=-1456928&class_interval=1&dest_id=-1456928&dest_type=city&group_adults=2&group_children=0&label_click=undef&nflt=oos%3D1%3B&no_rooms=1&raw_dest_type=city&room1=A%2CA&sb_price_type=total&search_selected=1&src=index&src_elem=sb&srpvid=74571920e19f02fb&ss=%C3%8Ele-de-France%2C%20France&ss_raw=ile-de-france&ssb=empty"

# Récupération du contenu HTML de la page
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# Recherche des éléments de la liste des hôtels
hotels = soup.findall("div", class="sr_property_block")

# Création d'un dictionnaire pour stocker les informations de chaque hôtel
dicthotels = {}

# Parcours de la liste des hôtels et extraction des informations nécessaires
for hotel in hotels:
    name = hotel.find("span", class="sr-hotelname").get_text().strip()
    starrating = hotel.find("span", class="sr-hoteltitle-badges").find("span", class_="invisible_spoken").gettext().strip()
    address = hotel.find("span", class="sr_card_address_line").get_text().strip()
    dict_hotels[name] = {"StarRating": star_rating, "Address": address}

# Enregistrement des données dans un fichier JSON
with open("Hotel_list.json", "w") as write_file:
    json.dump(dict_hotels, write_file, indent=4)
    
f=open("Hotel_list.json")

data=json.load(f)

def SortHotelAsList(dictionnaire):
    sortedHotel = dict(sorted(dictionnaire.items(), key=lambda item: item[1]["StarRating"], reverse=True))
    return list(sortedHotel.keys())

def TopHotel(dictionnaire,nbr=5):
    topHotelNameRatingPair=[]
    topHotel=SortHotelAsList(dictionnaire)[:nbr]
    for j in topHotel:
        topHotelNameRatingPair.append((j,dictionnaire[j]["StarRating"]))
    return topHotelNameRatingPair

def Get_Hotel_Adress(dictionnaire,hotel):
    return dictionnaire[hotel]["Address"]

def Get_Hotel_Rating(dictionnaire,hotel):
    return dictionnaire[hotel]["StarRating"]

print(TopHotel(data,5))
print(Get_Hotel_Rating(data,"hotel7"))
print(Get_Hotel_Adress(data,"hotel7"))

f.close()
