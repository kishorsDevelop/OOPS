import math
class Circle:
    radius = None
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return self.radius ** 2 * math.pi
    
    def perimeter(self):
        return self.radius * math.pi * 2

obj = Circle(8.3)
print(obj.area())
print(obj.perimeter())