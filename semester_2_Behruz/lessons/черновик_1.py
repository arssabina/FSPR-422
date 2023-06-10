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
    
    print('Instrument World ' + location + ' has:')
    print(str(sales_people) + ' sales employees')
    print(str(managers) + ' floor managers')

    try:
        ratio = sales_people / managers 
        print('The ratio of sales people to managers is ' + str(ratio))
    except ZeroDivisionError as err: 
        print("Error happened!")

        
   
    # print('The ratio of sales people to managers is ' + str(ratio))


for location, staff in staff.items():
    # Write your code below:

    print_staff_report(location, staff)
