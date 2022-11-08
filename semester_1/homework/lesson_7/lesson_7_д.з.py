# Set methods

# добавление 
a = {4,8,12,'apple'} 
a.add(5)
print(a)

a.update([54, 96,98,101])
print(a)

b={'banana', 'apricot', 'plum'}
a.update(b)
print(a)

# copy
a.copy()
print(a)

x=a.copy()
print(x)

# удаление

a.discard('plum')
print(a)

a.remove(101)
print(a)

a.pop()
print(a)

a.clear()
print(a)

# difference
a = {4,8,12,'apple'} 
b = {'apple', 4, 100,200,300,'banana'}
c=a.difference(b)
print(c)

a={5,6,9,'set'}
b={'set', 9, 11, 100}
c=b.difference(a)
print(c)

# union
a={1,2,3}
b={4,5,6,2}
c={3,7,8,9,1}
d=a.union(b,c)
print(d)

# Dictionary methods

# copy
fruits = {
    "apple" :   'red',
    "banana":   'yellow',
    "kivi"  :   'green'
}
fruits.copy()
print(fruits)

#item
pair= fruits.items()
print(pair)

#keys
k=fruits.keys()
print(k)

k=fruits.keys()
fruits ["plum"] ='purple'
print(k)

# get
g=fruits.get("kivi")
print(g)

persimmon=fruits.get("persimmon", "orange" )
print(persimmon)

#pop
fruits.pop("banana") 
print(fruits)

#popitem
fruits.popitem()
print(fruits)

#fromkeys
fruits = {'apple','banana', 'kivi'}
taste = 'yummy'
f=dict.fromkeys(fruits,taste)
print(f)

#update
fruits = {
    "apple" :   'red',
    "banana":   'yellow',
    "kivi"  :   'green'
}
fruits.update({"avocado": 'dark green'})
print(fruits)

#values
v=fruits.values()
print(fruits)


#clear
fruits.clear()
print(fruits)



