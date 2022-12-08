# https://www.codewars.com/kata/54ba84be607a92aa900000f1/train/python
# isIsogram "Dermatoglyphics" = true
# isIsogram "moose" = false
# isIsogram "aba" = false 

# def is_isogram(s):
#     isogram_s=set(s.lower())
#     if len(isogram_s)==len(s):
#        print (True)
#     else: 
#         print(False)

# is_isogram("Hello")

# =======================================================================
# https://www.codewars.com/kata/563cf89eb4747c5fb100001b/train/python
# Input: [1,2,3,4,5], output = [2,3,4,5]
# Input: [5,3,2,1,4], output = [5,3,2,4]

# def remove_smallest(numbers):
#     copy_of_numbers=numbers.copy()
#     if not (copy_of_numbers):
#         print(copy_of_numbers)
#     else:
#         copy_of_numbers.remove(min(copy_of_numbers))
#         print(copy_of_numbers)

# remove_smallest([1, 2, 3, 4, 5])

# =========================================================================
# https://www.codewars.com/kata/57cebe1dc6fdc20c57000ac9/solutions/python

# def find_short(s):
#     result=len(min(s.split(),key=len))
#     print(result)

# find_short("bitcoin take over the world maybe who knows perhaps")