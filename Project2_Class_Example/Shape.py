class Shape():
    """
    A class for defining basic shapes
    
    """
    def __init__(self, name="Unnamed Shape", NumberOfSides=3):
        self.name = name
        self.sides = NumberOfSides

    """
    Returns a string containing Shape Name and Number of Sides
    """
    def __str__(self):
        return "Shape : " + self.name + ", has " + str(self.sides) + " number of sides"
    