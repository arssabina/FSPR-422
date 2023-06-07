import json 
"""We can decode and encode json files into python objects"""

# Reading
with open("purchase_1_json") as purchase_json: 
    # convert data into python dict
    purchase_data = json.load(purchase_json)


print(purchase_data, purchase_data["user"])


# Writing a json file
turn_to_json = {
    "eventId": 674189,
    "dateTime": "2015-02-12T09:23:17.511Z",
    "chocolate": "Semi-sweet-dark",
    "IsTomatoAFruit": True, 
}


# import json
with open ("output.json", "w") as json_file: 
    json.dump(turn_to_json, json_file)
