import json

person = {
    "name": "john",
    "age": 50,
    "city": "New York"
}

with open("data.json","w") as file:
    json.dump(person,file,indent=4)

with open("data.json","r") as file:
    loaded_data = json.load(file)
    print(loaded_data)
    print(loaded_data['name'])