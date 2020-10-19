import math

class Point:
    def __init__(self, x, y):
        self.x=x
        self.y=y

    def distance(self, b):
        return math.sqrt((b.x-self.x)**2 + (b.y-self.y)**2)

    def move(self, x1, y1):
        self.x=x1
        self.y=y1
    def __repr__(self):
        return(f"P=({self.x},{self.y})")

if __name__=="__main__":
    a=Point(7,1)
    b=Point(1,1)
    print(a.distance(b))

    a.move(2,2)
    print(a)     
