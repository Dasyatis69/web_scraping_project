import random
import json

dict_Hotel={}
n=10

for i in range(1,n+1):
    Nom="hotel"+str(i)
    Star=str(random.randint(1,50)/10)
    Address=str(i)+" rue de la Paix, Paris"
    dict_Hotel[Nom] = {"StarRating": Star, "Address": Address}

with open("Hotel_list.json", "w") as write_file:
    json.dump(dict_Hotel, write_file, indent=4)

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