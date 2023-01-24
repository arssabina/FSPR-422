class OverloadingOperators:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)

    """Arithmetic operators"""
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return OverloadingOperators(x,y)
    
    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        return OverloadingOperators(x,y)

    def __mul__(self, other):
        x = self.x * other.x
        y = self.y * other.y
        return OverloadingOperators(x,y)

    def __truediv__(self, other):
        x = self.x / other.x
        y = self.y / other.y
        return OverloadingOperators(x,y)

    def __floordiv__(self, other):
        x = self.x // other.x
        y = self.y // other.y
        return OverloadingOperators(x,y)

    def __pow__(self, other):
        x = self.x ** other.x
        y = self.y ** other.y
        return OverloadingOperators(x,y)

    def __mod__(self, other):
        x = self.x % other.x
        y = self.y % other.y
        return OverloadingOperators(x,y)

    """Comparison Operators"""
    def __lt__(self, other):
        self_mag = (self.x * 2) + (self.y * 2)
        other_mag = (other.x * 2) + (other.y * 2)
        return self_mag < other_mag

    def __gt__(self, other):
        self_mag = (self.x * 2) + (self.y * 2)
        other_mag = (other.x * 2) + (other.y * 2)
        return self_mag > other_mag  

    def __eq__(self, other):
        self_mag = (self.x * 2) + (self.y * 2)
        other_mag = (other.x * 2) + (other.y * 2)
        return self_mag == other_mag 

numbers_1 = OverloadingOperators(12,6)
numbers_2 = OverloadingOperators(3,6)

print("Result of __add__ operator:", numbers_1 + numbers_2)
print("Result of __sub__ operator:", numbers_1 - numbers_2)
print("Result of __mul__ operator", numbers_1 * numbers_2)
print("Result of __truediv__ operator:", numbers_1 / numbers_2)
print("Result of __floordiv__ operator:", numbers_1 // numbers_2)
print("Result of __pow__ operator:", numbers_1 ** numbers_2)
print("Result of __mod__ operator:", numbers_1 % numbers_2)
print("Result of __lt__ operator:", numbers_1 < numbers_2)
print("Result of __gt__ operator:", numbers_1 > numbers_2)
print("Result of __eq__ operator:", numbers_1 == numbers_2)

