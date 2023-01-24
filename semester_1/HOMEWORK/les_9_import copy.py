
# 2 - задание
# for num in [1,2,3,4,5,6,7]:
#     print(num*4)
# ============================================================
  
import copy
s_1 = [1, 2, "hello", 4, 5, 6, 7]
s_2= copy.deepcopy(s_1)
for i in s_2:
    print(i*4)

# ===============================================================
# s_1 = [1, 2, "hello", 4, 5, 6, 7]
# s_2=s_1.copy()
# if isinstance (s_2,(str,tuple)):
#     for i in s_2: 
#         print(i)

# x=s_2.index("hello")
# print(x)

# print(s_2)


# import copy 
# a = ["a", "b", "c", "d", "e"]
# b = copy.copy(a) 
# for item in a:
#     print (item) 
#     b.remove(item) 
#     a = copy.copy(b)

# for i in s_2 [:]:
# s_2.remove("hello")
    # print (s_2) 


# for val in [1, 2, 3, 4, 5, [6, 7, 8, 5, 6], (4, 5, 6)]: 
#     print(val) 
#     if isinstance(val, (list, set, tuple)): 
#         for i in val: 
#             print(i)  

        

            


