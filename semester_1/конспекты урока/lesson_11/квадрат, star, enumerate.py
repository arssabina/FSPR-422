# **** 
# *  * 
# *  * 
# **** 
# **** 
# *  * 
# *  * 
# # **** 
# работает с принтами
# square_line = 4 
# star = "*" 
# star_width = star * square_line 
# print(star_width) 
# print(f"{star}  {star}") 
# print(f"{star}  {star}") 
# print(star_width) 
# for i in range(square_line): 
#     print(star, end="")

# 2-способ   (Правильный вариант)
square_line = 6 
star = "*" 
star_width = star * square_line
for i in range(square_line):
    # print("i=", i)
    if i>0 and i< (square_line-1): 
        empty_space = " " * (square_line-2)
        print(f"{star}{empty_space}{star}")
    else: 
        print(star*square_line)



# i=0
# while i < 10:
#     print("i=", i)
#     i +=1


# i = 0
# while True:
#     i +=1
#     print("i=", i)
#     if i ==100:
#         break

# names=[1,2,3,4,5,6]    в питоне так не деляется ,так код не пишем 
# i=0
# while i<len(names):
#     print(names[i])
#     i +=1


# for i, val in enumerate ("ABCDEFG"):
#     print(i,val)

