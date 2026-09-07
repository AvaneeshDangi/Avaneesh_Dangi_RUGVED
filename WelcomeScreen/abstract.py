from abc import ABC, abstractmethod


class Shape(ABC):

    def __init__(self, c):
        self.color = c

    def get_color(self):
        return self.color

    @abstractmethod
    def get_area(self):
        pass


class Square(Shape):

    def __init__(self, c, side):
        super().__init__(c)
        self.side = side

    def get_area(self):
        return self.side * self.side


# Driver code
color = input("Enter color: ")
side = float(input("Enter side: "))

square = Square(color, side)

print("Color:", square.get_color())
print("Area:", square.get_area())