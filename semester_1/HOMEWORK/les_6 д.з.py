# Tuple Methods

# Count method - для определения кол-ва вхождений определен.элемента

a = (1,2,3,4,5,3,3,58)
print(a.count(3))

a = (1,2,3,4,5,3,3,58)
x=a.count(3)
print(x)

a = 1,2,3,4,5,3,3,58
print(a.count(3), type (a))

a = ('abb', 'acc', 'abb')
print(a.count('abb'))


# Index method - выводит под каким индексом было первое вхождение опред.элемента

  #   0  1   2   3   4       5
a = ( 1, 2, 10, 50, 'ABC', 'python')
print(a.index(10))

  #   0  1   2   3   4       5
a = ( 1, 2, 10, 50, 'ABC', 'python')
x = a.index('ABC')
print(x)
  
  # 0  1   2   3   4       5
a = 1, 2, 10, 50, 'ABC', 'python'
print(a.index('python'), type(a))

