import json

with open('purchase_14781239.json') as purchase_json:
    purchase_data = json.load(purchase_json)

# Prints 'ellen_greg'
print(purchase_data['user'])

print(purchase_data['action'])

print(purchase_data['item_id'])



with open('message.json') as message_json:
    message = json.load(message_json)

print("\n")
print(message['text'])
