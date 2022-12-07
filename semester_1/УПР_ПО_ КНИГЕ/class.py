class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type

    def describe_restaurant(self):
        pass

    def open_restaurant(self):
        """ Выводит сообщение об открытии ресторана"""
        print(self.restaurant_name + " is open from 11:00 till 23:00 every day. " + "Come and enjoy " + self.cuisine_type)

restaurant=Restaurant("TARHAN UYGUR RESTAURANT", "Uygur cuisine")
restaurant.open_restaurant()

class Car():
    """Простая модель автомобиля."""

    def __init__(self, make, model, year):
        """Инициализирует атрибуты описания автомобиля."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
 
    def get_descriptive_name(self):
        """Возвращает аккуратно отформатированное описание."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    
    def update_odometer(self, mileage):
        """Изменяет значение аттрибута odometer reading посредством метода"""
        self.odometer_reading=mileage

    def read_odometer(self):
        "Выводит пробег машины в милях"
        print("This car has " + str(self.odometer_reading) + " miles on it.")
 
my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

# Изменение значения аттрибута 1-способ: 
# my_new_car.odometer_reading=23  # присваивается новое значению аттрибуту odometer_reading

# 2-способ: Создаем метод, который будет изменять значение аттрибута:
my_new_car.update_odometer(24)
print(my_new_car.read_odometer())
