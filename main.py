#crawl sgcarmart car data into an array of objects
from bs4 import BeautifulSoup
import requests
import json
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')

db = client.cars
bmws = db.bmw

numberOfRecords = 0

sgcarmart_url = 'https://www.sgcarmart.com/used_cars/listing.php?BRSR='+ str(numberOfRecords) +'&MOD=bmw&RPG=100&AVL=2'
carro_url = 'https://carro.sg/buy-car?page=1&query=BMW&sortBy=carro_showroom_sort_newest'

page_response = requests.get(carro_url, timeout=5)

data = BeautifulSoup(page_response.content, "html.parser")























# car_name = data.find_all('div', 
# style=lambda value: value and 'width:186px' in value and 'padding-left:4px' in value)

# car_price = data.find_all('div',
# style=lambda value: value and 'width:67px' in value and 'font-weight:bold' in value)


# def getData():
#     list_car = []
#     for name in car_name:
#         print(name.find('a').text)
#         car_name = name.find('a').text
#         records = {
#             'car_name' : car_name
#         }
#         list_car.append(records)

#     print(len(list_car))
#     bmws.insert_many(list_car)




# print(list_car)
# print(type(list_car))


#Encode data to JSON
# with open('data.json', 'w') as outfile:
#     json.dump(list_car, outfile, indent=4)







    
