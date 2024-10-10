# Let’s say we had a Python dictionary we wanted to save as a JSON file:
turn_to_json = {
    'eventId': 674189,
    'dateTime': '2015-02-12T09:23:17.511Z',
    'chocolate': 'Semi-sweet Dark',
    'isTomatoAFruit': True
}

# We’d be able to create a JSON file with that information by doing the following:
import json

with open('output.json', 'w') as json_file:
    json.dump(turn_to_json, json_file)

data_payload = [
    {
        'interesting message': 'What is JSON? A web application\'s little pile of secrets.',
        'follow up': 'But enough talk!'
    }
]

with open('data.json', 'w') as data_json:
    json.dump(data_payload, data_json)
