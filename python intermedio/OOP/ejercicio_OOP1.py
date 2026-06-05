import math
class Circle:
    def __init__(self,radius):
        self.radius = radius

    def get_area(self):
        return math.pi*(self.radius**2)


my_circle=Circle(50)
area=my_circle.get_area()
print(f"{area:.2f}")