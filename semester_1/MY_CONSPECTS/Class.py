class Person:
    def print_info(self, n): #"n - сколько раз должна выводиться информация каждого объекта"
        for i in range(n): # цикл, для того чтобы выводить информация n -количество раз
            print(f"Name: {self.name}, Surname: {self.surname}, Place of birth: {self.place_of_birth}")
    
    def get_age(self, current_year):
        print(f"Age: {current_year - self.year_of_birth}")



p1 = Person()
p1.name = "Sabina"
p1.surname = "Arshidinova"
p1.place_of_birth = "Uzbekistan"
p1.year_of_birth = 1986

print(p1.print_info(2))
print(p1.get_age(2022))  # возраст человека


