def hello():
    print("Greetings")

hello()


def hello_2(func):
    func()
    return 2

hello()
print(hello_2(hello))


# ==========================================

def wrapper():
    def hello_world():
        return 'Hello World!'
    return hello_world()

print(wrapper())       # Hello World!

print(hello_2(wrapper))   # разбор debugging


# ===============================
def like():
    print("Greetings")

hello()


def authorize(func):
    def wrapper(*args, **kwargs):
        print('расширяем функционал')
        print('расширяем функционал')
        return func(*args, **kwargs)
    return wrapper

# answer = authorize(like)  # wrapper
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




