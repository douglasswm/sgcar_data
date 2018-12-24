from requests import get
from bs4 import BeautifulSoup as bs
import json
from time import sleep
from time import time
from random import randint
from IPython.core.display import clear_output
from warnings import warn

url = 'https://www.sgcarmart.com/used_cars/listing.php?BRSR=1000&RPG=100'
response = get(url)

html_soup = bs(response.text, 'html.parser')
# print(html_soup)

data = html_soup.select("#contentblank > table")[0].find_all('table',{"width":"100%"},cellpadding = 0,cellspacing = 0,border = 0, style=lambda value: value and 'table-layout: fixed' in value)
# print(len(data))
test = data[0].find('td', align="center", width= "82", valign= "top").find('font', {'color':'#009900'})
print(test)
# start_time = time()
# requests = 0

# for _ in range(5):
#     # A request would go here
#     requests += 1
#     sleep(randint(1,3))
#     current_time = time()
#     elapsed_time = current_time - start_time
#     print('Request: {}; Frequency: {} requests/s'.format(requests, requests/elapsed_time))
#     clear_output(wait = True)

# warn("Warning Simulation")    