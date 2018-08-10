
import requests
from pprint import pprint
from PIL import Image

n = input("enter a city name: ")

url_getID = 'https://www.metaweather.com/api/location/search/?query=' + n
id_data = requests.get(url_getID)
d=dict(id_data.json()[0])
location_id = d['woeid']


#location_id = '44418'
url = 'https://www.metaweather.com/api/location/' + str(location_id) + '/'

data = requests.get(url)
w_data = data.json()
pprint(w_data)

print("\n")
print("the weather for " + w_data['title'] + " for the next 5 days:\n")
for x in w_data['consolidated_weather']:
	print(x['applicable_date'])
	print(x['weather_state_name'])
	print(x['weather_state_abbr'])

