# You take your son to the forest to see the monkeys. You know that there are a certain number there (n), but your son is too young to just appreciate the full number, he has to start counting them from 1.
# As a good parent, you will sit and count with him. Given the number (n), populate an array with all numbers up to and including that number, but excluding zero.
# For example(Input --> Output):
# def monkey_count(n):
    #your code here
   

# def monkey_count(n):
#     result = []
#     for num in range(1, n + 1):
#         result.append(num)
#     print(result)

# monkey_count(6)

# Create a function which answers the question "Are you playing banjo?".
# If your name starts with the letter "R" or lower case "r", you are playing banjo!

# The function takes a name as its only argument, and returns one of the following strings:

# name + " plays banjo" 
# name + " does not play banjo"
# Names given are always valid strings.

# def are_you_playing_banjo(name):
#     # Implement me!
#     # return name
#     for i in name:
#         if i[0] == "R" or "r": 
#             print(name + "plays banjo")
#         else: 
#             print(name + "does not play banjo")
        
# are_you_playing_banjo("Sabina")
# =============================================================================
# name = "Asmira"
# first_letter=name.find("R" and "r")
# if first_letter==0:
#     print(name + " plays banjo")
# else: 
#     print(name + " does not play banjo")
# ==========================================================================
def are_you_playing_banjo(name):
    first_letter=name.title().find("R")
    if first_letter == 0: 
        print (name.title() + " plays banjo")
    else: 
        print(name.title() + " does not play banjo")      

are_you_playing_banjo("rara")