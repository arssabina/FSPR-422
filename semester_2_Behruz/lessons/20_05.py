# data={
#     'USERS': 'Sabina',
#     'username': 'Sabina',
#     'password': 123456,
# }


# def authorize(username, password):
#     def decorator_authorize(func):
#         def wrapper(*args, **kwargs):
#             for item in data['users']:
#                 if item['username'] == username and item['password'] == password:
#                     return func(*args, **kwargs)
#                 else:
#                     return 'Wrong credentials!\n\nPlease, check your data and resubmit your purchase!'
                
#         return wrapper
    
#     return decorator_authorize

# @authorize(username='user_1', password=1002030)
# def like():
#     print("liked")

# like()
# ===========================================================

# import time

# def check_time(func):
#     def wrapper(a, b):
#         start=time.time()
#         func(a, b)
#         finish = time.time()
#         dt = finish - start
#         print("Время работы на функцию: " + str(dt))

#     return wrapper


# @check_time
# def multiply(a, b):
#     a*b

# multiply(20,2000000999999999990)
# =========================================================

# from functools import wraps


# def count_time(func):
#     @wraps(func)
#     def wrapper_decorator(*args, **kwargs):
#         """A wrapper function"""
#         start = time.timevalue = func(*args, **kwargs)
#         value = func(*args, **kwargs)
#         end = time.time()
#         print(end-start, "time passed")
#         return value
#     return wrapper_decorator


# @count_time
# def hello(a, b): 
#     """"Greats peson"""
#     for i in range(100):
#         i += 1
#     return i


# print(hello.__name__)
# print(hello.__doc__)
# x = count_time(hello)
# x.__name__
# x.__doc__


# try:
#     x = 10
#     y = 0
#     answer = x/y
# except:
#     print("Error happened!")

# print("Works")



try:
    x = 10
    y = 0
    answer = x/y
except ZeroDivisionError:
    print("Error happened!")

print("Works")


# try:
#     x = 10
#     y = 20
#     answer = x/y
#     raise ZeroDivisionError   
# except ZeroDivisionError:
#     print("Error happened!")

# print("Works")
   

