# ======================  REMOVE DUPLICATES  ==================================================
# To remove duplicates from a list we can create a dictionary, using the List items as keys.
# This will automatically remove any duplicates because dictionaries cannot have duplicate keys

# 1-method:

# pets=['dog', 'cat', 'goldfish', 'cat', 'rabbit', 'cat']
# pets=list(dict.fromkeys(pets))  
# print(pets)

# 2-method: to remove duplicates we can use set:
# pets=['dog', 'cat', 'goldfish', 'cat', 'rabbit', 'cat']
# pets=list(set(pets))
# print(pets)

b=[1,2,3,4,5,6,1,2,3,4, "AA", "BB", "AA"]
print(b, set(b), sep="\n")

print(b, list(set(b)), sep="\n")









