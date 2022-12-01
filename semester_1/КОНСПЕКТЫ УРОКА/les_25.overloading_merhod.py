"""Method overloading - Перегружение метода""" 

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # def __str__(self):
        # return f"Class info: name={self.name} age={self.age}"

    def __repr__(self):
        return f"Class info: name={self.name} age={self.age}"

person = Person("Sabina", 36)
person_2= Person("Bohir", 36)
print(person, person_2)       # если мы используем метод __str__, мы можем print писать так, чем печатать : print(person.name, person.age)
                            # мы также можем использовать метод __repr__ 
                            
# import datetime
# date = datetime.datetime.now()
# print(date, repr(date))

