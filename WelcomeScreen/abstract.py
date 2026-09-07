from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def get_area(self):
        pass

    def get_color(self):
        return self.color


class Square(Shape):

    def get_area(self):
        return self.side * self.side


color = input("Enter color: ")
side = float(input("Enter side: "))

square = Square()

square.color = color
square.side = side

print("Color:", square.get_color())
print("Area:", square.get_area())