# class Marker:
#     size=15 # статичная переменная,  которая определяется до вызова
#     health=10
#     # функции - методы
#     # переменные - аттрибуты
#     def __init__(self,company,color, price):
#         self.company = company
#         self.color = color   
#         self.price=price

#         # метод класса
#     def draw(self, line_length):
#         if self.health <=0:
#             return "Маркер истощён" 
#         self.health-=line_length


# # динамичные аттрибуты, которые опред-ся после вызова функции 
# marker=Marker("Marker Inc.", "blue", 120)
# marker_2=Marker("Best_markers.Inc.", "red", 100)
# marker_3=Marker("Your marker.Inc.", "black", 80)

# print(marker.company, marker.color, marker.price) 
# print(marker_2.company, marker_2.color, marker_2.price) 
# print(marker_3.company, marker_3.color, marker_3.price) 

# # не пишем print(self.company) потому что, self работает только внутри функции

# print("Health=", marker.health)
# marker.draw(5)
# print("Health=", marker.health)
# marker.draw(5)
# print("Health=", marker.health)
# marker.draw(5)
# print(marker.draw(11))
# print("Health=", marker.health)


class Human:
    date_of_birth = "12/02/1986"

    def __init__(self, height):
        self.name="Sabina"
        self.height=height

    def multiply(self, a, b):
        return a * b


print(Human.date_of_birth)   #этот аттрибут был создан до вызова класса     Вывод: #12/02/1986

# Создаём экземпляр/копию класса:  Когда мы создаём экземпляр класса, мы вызываем класс
human=Human(1.7)         
print(human)           # Вывод:      <__main__.Human object at 0x000002360D558970>
print(human.height, human.name)      # Вывод:    1.7 Sabina

print(human.multiply(15,30))   # вызываем метод класса и передаём два аргумента # Output:  450



