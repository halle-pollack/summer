import json

import requests
from pprint import pprint

bc = input("Enter the barcode: ")


url = 'https://world.openfoodfacts.org/api/v0/product/' + bc + '.json'

r = requests.get(url)

#print({} + '\n').format(r)
#print(r.text)
#print('\n')

pprint(r.json())

data = r.json()
print('\n')


ing = data["product"]['ingredients']
num_ing = str(len(ing))
product_name = data["product"]["product_name"]

print ("Your product is " + product_name + " and contains these " +  num_ing + " ingredients:\n")


for x in ing:
	print(x["text"])
	

