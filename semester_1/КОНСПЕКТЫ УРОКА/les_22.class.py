class Marker:
    size=15 # статичная переменная,  которая определяется до вызова
    # функции - методы
    # переменные - аттрибуты
    def __init__(self,company,color, price):
        self.company = company
        self.color = color   
        self.price=price

# динамичные аттрибуты, которые опред-ся после вызова функции 
marker=Marker("Marker Inc.", "blue", 120)
marker_2=Marker("Best_markers.Inc.", "red", 100)
marker_3=Marker("Your marker.Inc.", "black", 80)

print(marker.company, marker.color, marker.price) 
print(marker_2.company, marker_2.color, marker_2.price) 
print(marker_3.company, marker_3.color, marker_3.price) 

# не пишем print(self.company) потому что, self работает только внутри функции

