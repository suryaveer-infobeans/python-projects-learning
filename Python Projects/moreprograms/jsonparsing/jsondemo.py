import json

person = {
    "name": "john",
    "age": 50,
    "city": "New York"
}

json_data = json.dumps(person,indent=4)
print("JSON String\n",json_data)

parsed_data = json.loads(json_data)
print(parsed_data)
print(parsed_data['age'])