# https://www.codewars.com/kata/54ba84be607a92aa900000f1/train/python
# isIsogram "Dermatoglyphics" = true
# isIsogram "moose" = false
# isIsogram "aba" = false 

def is_isogram(s):
    isogram_s=set(s.lower())
    if len(isogram_s)==len(s):
        return True
    else: 
        return False

    # string = s.lower()
    # if len(s) == len(set(string)):
    #     return True
    # return False
is_isogram("Hello")
    