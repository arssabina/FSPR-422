numbers=[]
for i in range(100):
    numbers.append(i)
print("С циклом for", numbers)
"""Вместо этого кода можно использовать comprehension"""
numbers=[i for i in range(100)]
print("С методом comprehension", numbers)


def miltiply(i):
    return i*5

numbers=[i*5 for i in range(10)]
print(numbers)

numbers=[i*5 if i > 5 else False for i in range(10)]
print(numbers)

text=(("Hi", "Steve"), ("What's", "up?"))
print([word for sentence in text for word in sentence])

numbers=tuple(i*5 for i in range(10))  # tuple
print(numbers)
numbers={i*5 for i in range(10)}   # set
print(numbers)

numbers={i:i*5 for i in range(10)} # dict
print(numbers)

