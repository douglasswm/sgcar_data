from requests import get
from bs4 import BeautifulSoup as bs
import json
BRSR = 0

url = 'https://www.sgcarmart.com/used_cars/listing.php?BRSR=' + str(BRSR) + '&RPG=100'

# url = 'https://www.sgcarmart.com/used_cars/listing.php?RPG=20&ORD='
response = get(url)
# print(response.text[:500])

html_soup = bs(response.text, 'html.parser')
type(html_soup)

data = html_soup.select("#contentblank > table")[0].find_all('table',{"width":"100%"},cellpadding = 0,cellspacing = 0,border = 0, style=lambda value: value and 'table-layout: fixed' in value)
print(data)
print(len(data))

first_car = data[1]

first_car_model = first_car.strong.a.text.strip()
print('Model: '+first_car_model)

first_car_price = first_car.find('td', class_ ='font_red').div.text.strip()
print('Price: '+first_car_price)

first_car_depreciation = first_car.find('div', style=lambda value: value and 'width:101px' in value).text.strip()
print('Depreciation: '+first_car_depreciation)

first_car_reg_date = first_car.find('div', style=lambda value: value and 'width:89px' in value).text.strip()
print('Reg Date: '+first_car_reg_date)

first_car_eng_cap = first_car.find('div', style=lambda value: value and 'width:84px' in value).text.strip()
print('Eng Cap: '+first_car_eng_cap)

first_car_mileage = first_car.find('div', style=lambda value: value and 'width:83px' in value).text.strip()
print('Mileage: '+first_car_mileage)

first_car_veh_type = first_car.find('a', class_ = 'link_black nounderline').text.strip()
print('Veh Type: '+first_car_veh_type)

first_car_status = first_car.find('td', align="center", width= "82", valign= "top").div.strong.text.strip()
print('Status: '+ first_car_status)

#Need to clean the data of Posted:
first_car_ad_posted_date = first_car.find('td', class_ = 'font_gray_light font_10').text.strip()
print(first_car_ad_posted_date)
results = []
for car in data:

    if car.find('div', style=lambda value: value and 'width:67px' in value and 'font-weight:bold' in value) is not None:
        
        model = car.strong.a.text.strip()
        price = car.find('div', style=lambda value: value and 'width:67px' in value and 'font-weight:bold' in value).text.strip()
        depreciation = car.find('div', style=lambda value: value and 'width:101px' in value).text.strip()
        reg_date = car.find('div', style=lambda value: value and 'width:89px' in value).text.strip()
        eng_cap = car.find('div', style=lambda value: value and 'width:84px' in value).text.strip()
        mileage = car.find('div', style=lambda value: value and 'width:83px' in value).text.strip()
        veh_type = car.find('a', class_ = 'link_black nounderline').text.strip()
        status = car.find('td', align="center", width= "82", valign= "top").div.strong.text.strip()
        # posted_date = car.find('td', class_ = 'font_gray_light font_10').text.strip()

        car_data = {
            'model' : model,
            'price' : price,
            'depreciation' : depreciation,
            'registrationDate' : reg_date,
            'engineCapacity' : eng_cap,
            'mileage' : mileage,
            'vehicleType' : veh_type,
            'status' : status
        }

        results.append(car_data)

#Encode data to JSON
with open('data.json', 'w') as outfile:
    json.dump(results, outfile, indent=4)