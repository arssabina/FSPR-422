# ФУНКЦИЯ DEF

# def greet_user():
#     """Выводит простое приветствие."""
#     print("Hello!") 
# greet_user()

def myFun(arg1, **kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))
 
 
# Driver code
myFun("Hi", first='Geeks', mid='for', last='Geeks')

