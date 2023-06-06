USERS = [
    {
        'name': 'Behruz',
        'password': '234fjfdsd',
        'email': 'behruz@gmail.com',
        'purchases': [],
        'card': {'code': '3647583465734283', 'balance': 1000}
    }
]


import csv
with open ('store_users.csv', 'w', newline='', encoding ='utf-8') as store_users_csv:
    fields = ['name', 'password', 'email', 'purchases', 'card']
    users_writer = csv.DictWriter(store_users_csv, fieldnames=fields)
    users_writer.writeheader()
    for item in USERS: 
        users_writer.writerow(item)


PRODUCTS = [
    {
        "product_name": "sweater",
        "count": 10,
        "price": 100,
        "color": "black",
    },
    {
        "product_name": "sweater",
        "count": 10,
        "price": 100,
        "color": "black",
    }
]



import csv
with open ('products.csv', 'w', newline='', encoding ='utf-8') as products_csv:
    fields = ['product_name', 'count', 'price', 'color']
    products_writer = csv.DictWriter(products_csv, fieldnames = fields)
    products_writer.writeheader()
    for item in PRODUCTS: 
        products_writer.writerow(item)


import csv
with open ('products.csv', newline ='') as products_csv:
    products_reader = csv.DictReader(products_csv, delimiter=',')
    for row in products_reader:
        print(row['product_name'])