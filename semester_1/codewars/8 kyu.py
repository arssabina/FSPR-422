# You are given two interior angles (in degrees) of a triangle.
# Write a function to return the 3rd.
# Note: only positive integers will be tested.
# https://en.wikipedia.org/wiki/Triangle

# def other_angle(a, b):
#     third_angle=180-a-b
#     print (third_angle)

# other_angle(60,40)

# ===========================================================
# Write function bmi that calculates body mass index (bmi = weight / height2).
# if bmi <= 18.5 return "Underweight"
# if bmi <= 25.0 return "Normal"
# if bmi <= 30.0 return "Overweight"
# if bmi > 30 return "Obese"

# def bmi(weight, height):
#     result=weight/height**2
#     if result<=18.5: 
#         print ("Underweight")
#     elif result<=25.0:
#         print("Normal")
#     elif result<=30.0:
#         print("Overweight")
#     elif result>30:
#         print("Obese") 
# bmi(58,173)
# ==================================================================
# Нахождение суммы чисел из двух срок
# def sum_str(a, b):
#     if a=="":
#         a=0
#     if b=="":
#         b=0
#     s=str(int(a) + int(b))
#     print(s, type(s))


# sum_str("4", "5")

# +========================================================================

# def switch_it_up(number):
#     from_one_to_ten=['zero','one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
#     print(from_one_to_ten[number])

# switch_it_up(8)
# ============================================================================
# Remove First and Last Character
# def remove_char(s):
#     print(s[1:-1])

# remove_char("bbabyy")  # -> baby

# ===============================================================================

# Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.
# The output should be two capital letters with a dot separating them.
# It should look like this:
# Sam Harris => S.H
# patrick feeney => P.F

# def abbrev_name(name):
#     name_1=name.title().split()
#     print(name_1)
#     result=[]
#     for i in name_1: 
#         result.append(i[0])
#     print(".".join(result))

# abbrev_name('Arshidinova Sabina')

# =======================================================
# def string_to_number(s):
#     s=int(s)

#     print(s, type(s))

# string_to_number(18)
