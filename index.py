from bs4 import BeautifulSoup
import requests

# Here, we're just importing both Beautiful Soup and the Requests library
page_link = 'https://www.sgcarmart.com/used_cars/listing.php?MOD=bmw&PRC=0&DEP=0&RGD=0&VEH=0&AVL=2'

# this is the url that we've already determined is safe and legal to scrape from.
page_response = requests.get(page_link, timeout=5)

# here, we fetch the content from the url, using the requests library
data = BeautifulSoup(page_response.content, "html.parser")

#we use the html parser to parse the url content and store it in a variable.
car_name = data.find_all('div', style=lambda value: value and 'width:186px' in value and 'padding-left:4px' in value)

list_car = []
for name in car_name:
    print(name.find('a').text)
    list_car.append(name.find('a').text)
    print("SUCCESS=>>>")

print(list_car)
print(len(list_car))

    
