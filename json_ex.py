import json
from pprint import pprint

myObj = {
    "title": "Person",
    "type": "object",
    "properties": {
        "firstName": {
            "type": "string"
        },
        "lastName": {
            "type": "string"
        },
        "age": {
            "description": "Age in years",
            "type": "integer",
            "minimum": 0
        }
    },
    "required": ["firstName", "middleName", "lastName"]
}

pprint(myObj)

for x in myObj:
	print(x)