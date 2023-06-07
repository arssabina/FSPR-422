# import math 
# def litres(time):
#     return math.floor(time*0.5)
# print (litres(23))


# ========    Compare 2 digit numbers        =================

# https://www.codewars.com/kata/63f3c61dd27f3c07cc7978de/train/python

# MY SOLUTION
# def compare(a,b): 
#     a_res=sorted(list(str(a)))
#     b_res=sorted(list(str(b)))
#     print(a_res, b_res)
#     if a_res[0] == b_res[0] and a_res[1] == b_res[1]:
#         print("100%")
#     if a_res[0] == b_res[1] or a_res[1] == b_res[0]:
#         print("50%")
#     if a_res[0] == b_res[0] or a_res[1] == b_res[1]:
#         print("50%")
#     else: 
#         print("0%")
    
# compare(34,84)

# ======================================================
# BETTER SOLUTION
# def compare(a,b): 
#     a_sort=str(a)
#     b_sort=str(b)
#     if a_sort == b_sort: 
    #     print("100%")
    # if a_sort[0] in b_sort or a_sort[1] in b_sort: 
    #     print("50%")
    # else: 
    #     print("0%")

# compare(34,84)

# # ===================== with comprehension=========
# def compare(a,b): 
#     a_sort=str(a)
#     b_sort=str(b)
    # есть ошибка, надо исправить
    # print ("100%") if a_sort == b_sort else ("50%") if a_sort[0] in b_sort or a_sort[1] in b_sort else ("0%")

# compare(34,84)


# def alternate(n, first_value, second_value):
#     result = []
#     for i in range(n):
#         if i % 2==0: 
#             result.append(first_value)
#         else:
#             result.append(second_value)
#     print(result)

# alternate(3, True, False)

# ================remove duplicates and append dups to another list===================================================
# def duplicates(arr):
#     new_arr = []
#     dups = []
#     for i in arr:
#         if i not in new_arr:
#              new_arr.append(i)
#              print(new_arr, dups)
#         elif i not in dups:
#              dups.append(i)
    
#     print(dups)

# duplicates([1, 2, 4, 4, 3, 3, 1, 5, 3])

# ==============================
# def set_reduces(inp):
#     for i in inp: 
#         counter=inp.count(i)
#     print(counter)

# set_reduces([1,1,3,4,5,6,7])

# mylist = [5, 3, 5, 2, 1, 6, 6, 4] # the original input list with repeated elements.
# new_list=[]
# for x in mylist: 
#     c=mylist.count(x)
#     if c>1:
#         new_list.append(1)
# print(new_list)

# dup = {x for x in mylist if mylist.count(x) > 1}
# print(dup)
# #To count the number of list elements that were duplicated, you can run
# print(len(dup))

# =====================
# class List:
#     def remove_(self, integer_list, values_list):
#         #your code here
#         return []
# ============================

# Remove All The Marked Elements of a List
# https://www.codewars.com/kata/563089b9b7be03472d00002b/train/python

# def remove(integer_list, values_list):
#         result=[]
#         for i in integer_list: 
#             if i not in values_list:
#                 result.append(i)  
#         print(result)

# integer_list =  [1, 1, 2 ,3 ,1 ,2 ,3 ,4]
# values_list = [1, 3]

# remove(integer_list, values_list)


# Adding Arrays
# https://www.codewars.com/kata/59778cb1b061e877c50000cc/solutions


# def solution(text, ending):
#     check=text.endswith(ending)
#     print(check)

# solution("samurai", "ai")

# ========================  3 - зпадание ==================
def count(a):
    print("Counts the lists with len func:" , len(a))

a=[2, [2 , 3, [[[[[[[[5]]]]]]]]]]
count(a)
# =========================================
def count(a):
    counter=0
    for i in a: 
        if isinstance (i,(list)) :
            counter +=1
    print("Counts lists with counter:", counter)

a=[2, [2 , 3, [[[[[[[[5]]]]]]]]]]
count(a)
# ==================================

def positive_sum(arr):
    sum=0
    for i in arr: 
        if i>0:
            sum +=i
    print(sum)

positive_sum([-1,2,3,4,-5])