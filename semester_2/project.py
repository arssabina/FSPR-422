# 1-задание: 
days_in_week=7
number_of_days=input("Enter days: ")
years=int(number_of_days)//365
weeks=(int(number_of_days)%365) // days_in_week
days=(int(number_of_days)%365) % days_in_week
print("Years: " + str(years))
print("Weeks: " + str(weeks))
print("Days: " + str(days))

# --------------------------------------------------------------------------
# 2-задание
enter_the_str = input("Enter the string: ")
substr_search = input("Enter the substing to search: ")
if substr_search in enter_the_str: 
    print("The substring exists in the string")
else: 
    print("The substring doesn't exist in the string")
    
# ---------------------------------------------------------------------------
# 3-задание:
string=input("Enter the string: ")
abc='abcdefghijklmnopqrstuvwxyz'
counter=0
for val in abc: 
    if val not in string.lower(): 
        counter = 1
    else: 
        counter = 0

if counter == 1: 
    print("This string is NOT pangram")
else: 
    print("This string is pangram")
    
