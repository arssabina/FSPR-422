def hello():
    print("Greetings")

hello()


def hello_2(func):
    func() # вызов функции hello
    return 2

hello()
print(hello_2(hello))


# ==========================================

def wrapper():
    def hello_world():
        return 'Hello World!'
    return hello_world()  # внешн.функция возвращает ссылку на внутр.функцию

print(wrapper())       # Hello World!

print(hello_2(wrapper))   # разбор debugging


# ===============================
def like():
    print("Greetings")

def authorize(func):
    def wrapper(*args, **kwargs):
        # code
        # проверка регистрации пользователя
        print('расширяем функционал')
        print('расширяем функционал')
        return func(*args, **kwargs)
    return wrapper

# answer = authorize(like)  # wrapper  ссылка на внутр.функцию 
# print(answer)
# print(answer())


@authorize
def like(username):
    # логика лайка
    print(f"{username} liked post.")

# like()

@authorize
def buy(item, price):
    return item * price

# answer = authorize(buy)
# print("total = ", answer(2,20))
print("total = ", buy(1, 100))


# ================================================
from functools import wraps

def repeat(num_times): 
    def decorator_repeat(func):
        # wraps(func)
        def wrapper_repeat(*args, ** kwargs): 
            for _ in range(num_times): 
                value = func (*args, **kwargs)
            return value
        return wrapper_repeat
    return decorator_repeat


@repeat(num_times=3)
def hello():
    print("Greetings")
# answer = repeat(num_times=3)
# answer = answer(hello)
# print(answer())
# repeat(num_times=3)(hello)()
hello()