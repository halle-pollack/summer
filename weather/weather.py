
import requests
import datetime
from pprint import pprint
from PIL import Image, ImageDraw, ImageFont




week_pic = Image.new("RGBA", (120*6,210))
font = ImageFont.truetype('BebasNeue-Regular.ttf',16)


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
print("The weather for " + w_data['title'] + " for the next 5 days:\n")



def c_to_f(temp):
	return str(round((9/5)*temp + 32))

def get_dayOfWeek(dateStr):

	weekday_names = ["Monday", "Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

	d=datetime.datetime.strptime(dateStr,'%Y-%m-%d')
	return weekday_names[d.weekday()]

count = 0
for x in w_data['consolidated_weather']:

	date = x['applicable_date'][-5:]
	weather_state = x['weather_state_name']
	weather_state_abbr = x['weather_state_abbr']
	filename = weather_state_abbr + ".png"
	hi_temp = round(x['max_temp'])
	low_temp = round(x['min_temp'])

	pic=Image.open(filename)
	week_pic.paste(pic,(120*count,0))
	font.size=16
	w,h = ImageDraw.Draw(week_pic).textsize(weather_state)
	ImageDraw.Draw(week_pic).text(((120*count)+(120-w)/2 , 160),weather_state, font = font)
	w,h = ImageDraw.Draw(week_pic).textsize(date)
	ImageDraw.Draw(week_pic).text(((120*count)+(120-w)/2, 145),date, font = font)
	w,h = ImageDraw.Draw(week_pic).textsize("high: "+c_to_f(hi_temp))
	ImageDraw.Draw(week_pic).text(((120*count)+(120-w)/2, 175),"high: "+c_to_f(hi_temp), font = font)
	w,h = ImageDraw.Draw(week_pic).textsize("low: " +c_to_f(low_temp))
	ImageDraw.Draw(week_pic).text(((120*count)+(120-w)/2 , 190),"low: " +c_to_f(low_temp), font = font)
	w,h = ImageDraw.Draw(week_pic).textsize(get_dayOfWeek(x['applicable_date']))
	
	ImageDraw.Draw(week_pic).text(((120*count)+(120-w)/2 , 130),get_dayOfWeek(x['applicable_date']), font =  ImageFont.truetype('BebasNeue-Regular.ttf',18))

	print(date)
	print(weather_state)
	print("Hi:" + c_to_f(hi_temp))
	print("Lo:" + c_to_f(low_temp))
	print("\n")
	count+=1

week_pic.show(title = "_week")