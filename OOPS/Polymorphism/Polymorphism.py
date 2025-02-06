# Example of Polymorphism
class shape:
    def area(self):
        pass

class square(shape):
    def __init__(self,side):
        self.side = side
    
    def area(self):
        return self.side * self.side
  
class circle(shape):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return 3.1425 * self.radius * self.radius

class rectangle(shape):
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth
    
    def area(self):
        return self.length * self.breadth

class triangle(shape):
    def __init__(self,base,height):
        self.base = base
        self.height = height
    
    def area(self):
        return 0.5 * self.base * self.height

shapes = [square(10), circle(9), rectangle(7,8), triangle(5,10)]
for shape in shapes:
    print(f"Area of {type(shape).__name__} is : {shape.area()}")
