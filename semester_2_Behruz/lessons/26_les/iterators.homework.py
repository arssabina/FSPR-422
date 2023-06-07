# ================================= с циклом for 

import time
def check_time(func):
    def wrapper():
        start = time.time()
        func()
        finish = time.time()
        dt = finish - start
        print("Wasted time with for cicle: " + str(dt))

    return wrapper

@check_time
def exponentiation():
    res = [i **2 for i in range(10000)]
    print(res)
        
exponentiation()


# ============================================================
# import time
# def check_time_1(func):
#     def wrapper():
#         start = time.time()
#         func()
#         finish = time.time()
#         dt = finish - start
#         print("Wasted time with iterator: " + str(dt))

#     return wrapper


# @check_time_1
# def s_iter():
#     numbers_iter = (i**2 for i in range(10000))
#     for num in numbers_iter:
#        print(num)

# s_iter()