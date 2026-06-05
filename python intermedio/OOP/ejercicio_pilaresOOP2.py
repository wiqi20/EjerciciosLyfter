from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def calculate_perimeter(self):
        pass
    @abstractmethod
    def calculate_area(self):
        pass

class Circle(Shape):
    def __init__(self,radius):
        self.radius= radius
    def calculate_area(self):
        area = math.pi*(self.radius**2)
        return area
    def calculate_perimeter(self):
        perimeter = 2*math.pi*self.radius
        return perimeter

class Square(Shape):
    def __init__(self,side):
        self.side= side
    def calculate_area(self):
        area = self.side**2
        return area
    def calculate_perimeter(self):
        perimeter = 4*self.side
        return perimeter

class Rectangle(Shape):
    def __init__(self,width,height):
        self.width= width
        self.height= height
    def calculate_area(self):
        area = self.width*self.height
        return area
    def calculate_perimeter(self):
        perimeter = 2*(self.width+self.height)
        return perimeter

ci=Circle(radius=5)
sq=Square(side=4)
re=Rectangle(width=3, height=6)
print(f"the circle area is: ", round(ci.calculate_area(),2))
print(f"the circle perimeter is: ", round(ci.calculate_perimeter(),2))
print(f"the Square area is: ", round(sq.calculate_area(),2))
print(f"the Square perimeter is: ", round(sq.calculate_perimeter(),2))
print(f"the Rectangle area is: ", round(re.calculate_area(),2))
print(f"the Rectangle perimeter is: ", round(re.calculate_perimeter(),2))