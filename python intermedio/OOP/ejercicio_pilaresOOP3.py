# la herencia multiple puede ser usada cuando se necesita combinar 
# comportamientos o atributos de mas de una clase padre, 
# sirve mucho en casos donde se necesita reutilizar codigo de distintas jerarquias 
# sin duplicar el codigo

from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def calculate_perimeter(self):
        pass
    @abstractmethod
    def calculate_area(self):
        pass

class Colored:
    def __init__(self, color="black"):
        self.color = color

    def show_color(self):
        return f"The color of the shape is {self.color}"

class Circle(Shape,Colored):
    def __init__(self,radius,color="black"):
        Shape.__init__(self)
        Colored.__init__(self, color)
        self.radius= radius

    def calculate_area(self):
        area = math.pi*(self.radius**2)
        return area

    def calculate_perimeter(self):
        perimeter = 2*math.pi*self.radius
        return perimeter

class Square(Shape,Colored):
    def __init__(self,side,color="black"):
        Shape.__init__(self)
        Colored.__init__(self, color)
        self.side= side
    def calculate_area(self):
        area = self.side**2
        return area
    def calculate_perimeter(self):
        perimeter = 4*self.side
        return perimeter

class Rectangle(Shape,Colored):
    def __init__(self,width,height,color="black"):
        Shape.__init__(self)
        Colored.__init__(self, color)
        self.width= width
        self.height= height
    def calculate_area(self):
        area = self.width*self.height
        return area
    def calculate_perimeter(self):
        perimeter = 2*(self.width+self.height)
        return perimeter

ci=Circle(radius=5, color= "red")
sq=Square(side=4, color= "blue")
re=Rectangle(width=3, height=6, color= "green")
print(f"the circle area is: ", round(ci.calculate_area(),2))
print(f"the circle perimeter is: ", round(ci.calculate_perimeter(),2))
print(ci.show_color())
print(f"the Square area is: ", round(sq.calculate_area(),2))
print(f"the Square perimeter is: ", round(sq.calculate_perimeter(),2))
print(sq.show_color())
print(f"the Rectangle area is: ", round(re.calculate_area(),2))
print(f"the Rectangle perimeter is: ", round(re.calculate_perimeter(),2))
print(re.show_color())