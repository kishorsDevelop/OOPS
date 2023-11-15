from abc import ABC, abstractmethod
import math

class Shape:
    
    def __init__(self):
          pass
    
    @abstractmethod
    def Area(self):
         pass
    
    @abstractmethod
    def Perimeter(self):
         pass   
    
class Circle(Shape):
     
    def __init__(self, radius):
          self.radius = radius
    
    def Area(self):
         return math.pi * self.radius ** 2

    def Perimeter(self):
         return 2 * math.pi * self.radius

class Triangle(Shape):
     
    def __init__(self, b, h, l):
          self.b = b
          self.h = h
          self.l = l

    def Area(self):
         return 0.5 * self.b * self.h

    def Perimeter(self):
         return self.l + self.b + self.h
     
class Square(Shape):
     
    def __init__(self, side):
          self.side = side
        
    def Area(self):
         return self.side * self.side
    
    def Perimeter(self):
         return 4 * self.side
    
def Factory(shape):
    
    area = 0
    perimeter = 0

    if shape == 'circle':
       radius = float(input("Enter radius: "))  
       area = Circle(radius).Area()
       perimeter = Circle(radius).Perimeter()

    elif shape == 'triangle':
       base = int(input('Enter base: '))
       height = int(input('Enter height: '))
       length = int(input('Enter length: '))
       area = Triangle(base, height, length).Area()
       perimeter = Triangle(base, height, length).Perimeter()
    
    else:
       side = int(input('Enter Side: '))
       area = Square(side).Area()
       perimeter = Square(side).Perimeter()
    
    print(area)
    print(perimeter)
      
if __name__ == '__main__':
     
    shape = input("Enter shape in lowercase letters: ")
    Factory(shape)

    

          
      
    