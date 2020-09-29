#! python3
# main.py - looks throuh pick n pull website for cars that i'm looking for.
# sends email when there is an update.

import requests, bs4, time
import selenium

website = 'https://www.picknpull.com/check_inventory.aspx?Zip=02905&Make=234&Model=4350&Year=&Distance=25&Lat=41.784005&Lon=-71.400250'

res = requests.get(website)

res.raise_for_status() # make sure response is 200

# time.sleep(1)

# cars = [] # list of cars at pick-n-pulls nearby

PNP_html = bs4.BeautifulSoup(res.text, 'html.parser')


print(PNP_html.select('.vehicle-year')[0].getText())

