import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.perimeter = 2*(math.pi)*(self.radius)
        self.area = (math.pi)*(self.radius ** 2)
    def get_perimeter(self):
        return self.perimeter
    def get_area(self):
        return self.area

class Cylinder(Circle):
    def __init__(self, radius, height):
        Circle.__init__(self, radius)
        self.height=height
    def get_volume(self):
        return (self.area)*(self.height)

if __name__=="__main__":
    circle1 = Circle(2)
    print(f"{circle1.get_perimeter()}, {circle1.get_area()}")        

    cilinder1 = Cylinder(2, 4)
    print(f"{cilinder1.get_perimeter()}, {cilinder1.get_area()}, {cilinder1.get_volume()}")        