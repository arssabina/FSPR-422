

# a,b,*args=(2,4,4,7,8,9,10)
# print(a,b,args)   # 2 4 [4, 7, 8, 9, 10]

# for i in range (10): # от 0 до 9
#     print (i)

# print("Next range")
# for i in range (4,10,2): # от 0 до 9 но с шагом +2 (4+2, 6+2)  Вывод: 4,6,8
#     print (i)


# print("list")
# numbers=[1,2,3,4,5,6,7]
# for i in range (len(numbers)):
#    numbers[i] *=4
#    print(numbers)


# # continue 
# numbers=[1,2,3,5,4,5,6,7]
# for val in numbers:
#     if val==5 or val==7: # val=5
#         print(f"пропустить {val}")
#         continue # -> for
#     print("val=", val)


    
# break   - выйти из цикла, закончить свою работу
numbers=[1,2,3,5,4,5,6,7]
for val in numbers:
    if val==5 or val==7: # val=5
        print(f"Выйти из цикла")
        break # -> for
    print("val=", val)


if 1==1:  
    pass    # Использ-ся для того чтобы не писать команды

