import math
class Circle:
    radius=50
    def get_area(self):
        area= math.pi*(self.radius**2)
        print(f"{area:.2f}")


my_circle=Circle()
my_circle.get_area()