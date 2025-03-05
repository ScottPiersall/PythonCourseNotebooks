from Shape import *

class Triangle(Shape):
    def __init__(self, name="", side1=1.0, side2=1.0, side3=1.0):
        super().__init__(name, 3)
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
    

    def Perimeter(self):
        return self.side1 + self.side2 + self.side3
    
    """
    Returns a string containing Triangle Name and Number of Sides
    """
    def __str__(self):
        return "TRIANGLE : " + self.name + ", has " + str(self.sides) + " number of sides"
