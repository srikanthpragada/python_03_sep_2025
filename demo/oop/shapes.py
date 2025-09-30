from abc import ABC, abstractmethod

# Abstract class
class Shape(ABC):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, x, y, w, l):
        super().__init__(x, y)
        self.w = w
        self.l = l

    def area(self):
        return  self.w * self.l


class Square(Shape):
    def __init__(self, x, y, s):
        super().__init__(x, y)
        self.s = s

    def area(self):
        return self.s * 2


r = Rectangle(10, 20, 10, 15)
print(r.area())

s = Square(20, 10, 15)
print(s.area())
