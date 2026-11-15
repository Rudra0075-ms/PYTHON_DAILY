import math
class circle:
    def __init__(self, radius):
        self.radius=radius
    def getArea(self):
        return round(math.pi*self.radius**2)
    def getPerimeter(self):
        return round(2*math.pi*self.radius)
circled=circle(11)
print(circled.getArea())
print(circled.getPerimeter())
                