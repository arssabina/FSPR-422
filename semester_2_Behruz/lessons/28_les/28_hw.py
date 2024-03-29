# 1. Используя исключения, исправьте код ниже
staff = {
    'Austin': {
        'floor managers': 1,
        'sales associates': 5
    },
    'Melbourne': {
        'floor managers': 0,
        'sales associates': 8
    },
    'Beijing': {
        'floor managers': 2,
        'sales associates': 5
    },
}

def print_staff_report(location, staff_dict):
    managers = staff_dict['floor managers']         # 1   0    2
    sales_people = staff_dict['sales associates']   # 5   8    5
    
    try:
        sales_people / managers 
    except ZeroDivisionError:
        print("Error happened!")
    else:
        print('The ratio of sales people to managers is ' + str(sales_people / managers))

    print('Instrument World ' + location + ' has:')
    print(str(sales_people) + ' sales employees')
    print(str(managers) + ' floor managers')
    # print('The ratio of sales people to managers is ' + str(ratio))


for location, staff in staff.items():
    # Write your code below:

    print_staff_report(location, staff)

# 2. Используя исключения, исправьте код ниже и создайте собственное исключение, которое должно вывести ошибку, если количество покупаемых больше количеств товаров в наличии. Также добавьте сообщение для созданного исключения с строкой: 'We don't' + str(self.supply) + ' in stock'
inventory = {
    'Piano': 3,
    'Lute': 1,
    'Sitar': 2
}

try:
    val = inventory['Guitar']
except KeyError:
    inventory['Guitar'] = 'Guitar'
    # print("Key error. But we can add it to the dict")

def submit_order(instrument, quantity):
    # supply = inventory[instrument]  # 0
   
    # Write your code below  
    try: 
        inventory[instrument] -= quantity
    except TypeError: 
        print('One of the variables is not an integer')
    else:
        print('Successfully placed order! Remaining supply: ' + str(inventory[instrument]))

instrument = 'Guitar'
quantity = 5
submit_order(instrument, quantity)

# 3. Написать регулярное выражения, для нахождения навыков программирования из данного списка слов
import re

titles = [
    "Middle JavaScript Developer",
    "Middleee JavaScript Developer (AngularJS 9)",
    "Middle JavaScript Developer (React)",
    "Seniorrr JavaScript Developer (Angular)",
    "middle JavaScript angularjs "
]

# Навыки которые мы должны найти: javascript, angularjs, react, node js, node.js, nodejs
# При этом регистр не имеет значения, то есть angularjs и Angularjs - должно рассматриваться одинаково

# 1. 
for key in titles: 
    # result = re.search('javasript', key, re.IGNORECASE)
    res = re.search('(?i)javascript', key)
    print(res)

# for key_1 in titles: 
#     # result = re.search('javasript', key, re.IGNORECASE)
#     res_1= re.findall('(?i)angularjs', key)
#     print(res_1)

# for key_3 in titles: 
#     result = re.search('react', key, re.IGNORECASE)
#     res = re.search('(?i)react', key)
#     print(res)

import re

title = 'Middle Javascript react'

js = {
    "Javascript": [
        "javascript",
        "angular", 
        "angularjs",
        "react",
        "node js",
        "node.js",
        "nodejs"
    ]
}
# (javascript)|(angular)|(angularjs)|(react)|(node_js)|(node.js)|(nodejs)|(nodejs)
mapper_string = "|".join([reg_ex for reg_ex in js["javascript"]])
result = re.finditer(mapper_string, title, re.IGNORECASE)
print(next(result))
print(next(result))


regex = r"react|javascript|angular"
test_str = "middle javasctipt react"
matches = re.findall(regex, test_str, re.MULTILINE)

# print(matches)
# for match in matches: 
#     print("match", match.group())

# print(len(matches))

pattern = r"(^[\sA - Z\d$#@%]{6,}\d$)"
password = "jsfuy4"

result = re.fullmatch(pattern, password.lower())
print(result)
