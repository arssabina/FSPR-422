print("tuple")
numbers=(1,2,3,4,5,6,7)
for num in numbers:
   print(num+2)


print("set")
numbers={1,2,3,4,5,6,7}
for num in numbers:
   print(num+2)

print("dict")
user={
    "name":  "George",
    "age":  25,
    "skill": "swim",
}
for key in user:
    print(key)

print("dict vals")
for val in user.values():
    print(val)

print("\ndict items")
for key,val in user.items():
    print("key=", key, "val=", val)
