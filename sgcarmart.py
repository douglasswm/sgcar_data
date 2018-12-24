from requests import get
from bs4 import BeautifulSoup as bs
import json
from time import sleep
from time import time
from random import randint
from IPython.core.display import clear_output
from warnings import warn
from pymongo import MongoClient
from pymongo.collection import ReturnDocument

#Initialise DB
client = MongoClient('mongodb://localhost:27017/')
db = client.sgcarmart
carsCollection = db.sgcarmart_cars

# Preparing the monitoring of the loop
start_time = time()
requests = 0
pages = [str(i) for i in range(0,100000,100)]


# For every page in the interval 100 records
for page in pages:

    # Make a get request
    url = 'https://www.sgcarmart.com/used_cars/listing.php?BRSR=' + page + '&RPG=100&AVL=2'

    # Test for sold cars data
    sold_cars_url = 'https://www.sgcarmart.com/used_cars/listing.php?BRSR=' + page + '&RPG=100&AVL=1'

    # Fetch page
    response = get(url)

    # Pause the loop
    sleep(randint(6,12))

    # Monitor the requests
    requests += 1
    elapsed_time = time() - start_time
    print('Request:{}; Frequency: {} requests/s'.format(requests, requests/elapsed_time))
    clear_output(wait = True)

    # Throw a warning for non-200 status codes
    if response.status_code != 200:
        warn('Request: {}; Status code: {}'.format(requests, response.status_code))
    
    html_soup = bs(response.text, 'html.parser')

    # Select all the car div from a single page
    data = html_soup.select("#contentblank > table")[0].find_all('table',{"width":"100%"},cellpadding = 0,cellspacing = 0,border = 0, style=lambda value: value and 'table-layout: fixed' in value)

    # Break the loop if no records on page
    if html_soup.find('td', width='175', height='160', valign='top') is not None:
        warn('===============NO MORE RECORDS===============') 
        print('===============NO MORE RECORDS===============') 
        break 
    
    #for each car div
    for car in data:

        #if price data is present, then:
        if car.find('div', style=lambda value: value and 'width:67px' in value and 'font-weight:bold' in value) is not None and car.find('td', align="center", width= "82", valign= "top").find('font', {'color':'#009900'}) is not None:
            
            model = car.strong.a.text.strip()
            price = car.find('div', style=lambda value: value and 'width:67px' in value and 'font-weight:bold' in value).text.strip()
            depreciation = car.find('div', style=lambda value: value and 'width:101px' in value).text.strip()
            reg_date = car.find('div', style=lambda value: value and 'width:89px' in value).text.strip()
            eng_cap = car.find('div', style=lambda value: value and 'width:84px' in value).text.strip()
            mileage = car.find('div', style=lambda value: value and 'width:83px' in value).text.strip()
            veh_type = car.find('a', class_ = 'link_black nounderline').text.strip()
            status = car.find('td', align="center", width= "82", valign= "top").div.strong.text.strip()
            posted_date = car.find('td', class_ = 'font_gray_light font_10').text.strip()

            car_data = {
                'model' : model,
                'price' : price,
                'depreciation' : depreciation,
                'registrationDate' : reg_date,
                'engineCapacity' : eng_cap,
                'mileage' : mileage,
                'vehicleType' : veh_type,
                'status' : status,
                'postedDate' : posted_date
            }

            update = carsCollection.find_one_and_update(car_data, {"$set":car_data},upsert=True,return_document=ReturnDocument.BEFORE)
            
            if update == None:
                print(update)
                print("===A RECORD HAS BEEN INSERTED INTO DB===")
            else:
                print("=====RECORD ALREADY EXIST=====")    
        

    # print('Number Of Cars: '+ str(len(results)))
    # carsCollection.insert_many(results)
    # print('===' + str(len(results)) + ' RESULTS INSERTED INTO DB===')
