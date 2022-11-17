
numbers = [1,2,3,4,'Hello', 5,6,7,9]
numbers.append("Hello")
print(numbers)

# Extend list by appending elements from the iterable
numbers.extend([2,3,4])
print(numbers)

numbers=numbers + [77,4]
# 1 + 2 = 3 
# "dsa" + "te" = "dsate" 
# print ( numbers*2)
# Полиморфизм

# count

numbers.pop() 
print(numbers)
numbers.remove('Hello')
numbers.remove('Hello')
print(numbers)
# numbers.remove('Tee')

number_of_occurence=numbers.count (3)
print('count', number_of_occurence)

numbers.sort()
print(numbers)

numbers.sort(reverse=True)
print(numbers)

words= ['foo', 'aga', 'ada', 'tall', 'Tall']
words.sort()
print(words)


# Матрица
[2,3,4,5,6] # вектор
matrix = [[2,3,4], [5,6,7]] # матрица 3 столбца и 2 строки
print(matrix [1][1]) 
# 2 3 4
# 5 6 7 
# random = list (1) # error
# random = list (True) # error

random = list ("Random jhklhli") # error
splitted_string = "Split me ! random".split("me ! ") # ' '  
print(random, splitted_string, ''.join(random), sep="\n")

# Tuple - кортеж (iterable)   похож на список, различие в том, что список это изменяемый тип данных, а кортеж не измен. 
# Кортеж защищает данные от преднамеренных изменений, экономит место, занимает меньше места, чем лист
# List - список пишется квадратными скобками, а кортеж tuple с помощью круглых скобок 

numbers=(2,3,4,5,6)
print(numbers, numbers [3])

#numbers[1] = "changed" 
# читать, создавать
numbers=(2,4,5, [4,5])
numbers[3][0] = 24
print(numbers[3], numbers [3][0])

#           0       1    2 3 4 
numbers=[[2,3,4], [5,6], 5,6,7]
numbers [0][2]

# 4 метода создания tuple
numbers = (2,3,4)  
print('1', type (numbers), numbers) 
numbers = tuple()
print(type (numbers), numbers) 
numbers=5,3,1
print('last', type (numbers), numbers) 

a=[2,3,5]
a=tuple(a)
print(type(a), a)
 


