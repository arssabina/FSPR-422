def hello():
    print("Greetings")

hello()


def hello_2(func):
    func()
    return 2

# hello()
print(hello_2(hello))

def wrapper():
    def hello_world():
        return 'Hello World!'
    return hello_world()

print(wrapper())       # Hello World!

print(hello_2(wrapper))   
