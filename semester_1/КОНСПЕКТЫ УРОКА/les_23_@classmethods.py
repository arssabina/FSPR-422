class PlayerCharacter: 
    membership = True
    def __init__(self, hobby, name='anonymous', age=0):
        self._hobby=hobby      #приватный аттрибут, его можно исп-ть только внутри класса
        self.name=name
        self.age=age
    


    def _welcome(self):   # приватная функция, прив.функции можно использовать только внутри класса
        return "HEEEEEEEEEEEYYY!"

    def shout(self):
        return f'{self._welcome()}. My name is {self.name} and my hobby is {self._hobby}.'

    


    @classmethod
    def adding_things_2(cls, num1, num2):
        return cls(num1, num2) 
        # cls это ссылка на сам класс PlayerCharacter
 
    # @staticmethod             аттрибуты не связаны с классом , то есть можно пистать без класса
    # позволяет методу не иметь ссылку на класс


    # def multiply (a, b):  не пишем self, потому что метод static не имеет ссылку на класс
    #     return a * b

player_1=PlayerCharacter("hiking","Jerry", 20)
print(player_1.shout())
# print(player_1._welcome())  # так делать нельзя, так писать код, потому что это приватный метод
# print(player_1.name, player_1.age)

# player_1=PlayerCharacter("Sabina")
# print(player_1.name, player_1.age)

# print(player_1.adding_things(2,5))
# print(PlayerCharacter.adding_things(2,5))
# print(PlayerCharacter.shout(PlayerCharacter))

# player_3=PlayerCharacter.adding_things_2("hello", "world") 
# print(player_3.age, player_3.name)


class Ship:
    def __init__(self, draft, crew):
        self.draft = draft
        self.crew = crew

    def is_worth_it(self):
        if self.draft - self.crew * 1.5 >=20:
            return True
        else: 
            return False

ship=Ship(5,10)
print(ship.is_worth_it())