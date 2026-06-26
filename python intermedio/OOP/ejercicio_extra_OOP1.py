import math

class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.validate_numbers()


    def validate_numbers(self):
        if self.width< 0 or self.height < 0:
            raise ValueError("Entered Value must be possitive")


    def get_area(self):
        return self.width*self.height


    def get_perimeter(self):
        return 2*(self.width+self.height)


try:
    re=Rectangle(300,-250)
    print(f"the rectangle area is: ",round(re.get_area(),2))
    print(f"the rectangle perimeter is: ",round(re.get_perimeter(),2))
except ValueError as e:
    print("Error: ",e)