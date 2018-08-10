import requests
import json
from pprint import pprint

base_url='http://httpbin.org/post'

#requests.get(base_url)

data_q = {
	 'name':'Halle P',
	 'age':21
	}



#requests.put(base_url,data=data_q)
#r=requests.put(base_url,data=data_q, json= fp)
r = requests.post(base_url, json={'my':'json'})
pprint(r.json())