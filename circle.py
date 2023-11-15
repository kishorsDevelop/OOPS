class Circle:
    radius = None
    pi = 3.14
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return self.radius * self.radius * self.pi
    
    def perimeter(self):
        return self.radius * self.pi * 2

obj = Circle(8.3)
print(obj.area())
print(obj.perimeter())