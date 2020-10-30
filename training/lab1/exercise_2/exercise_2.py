import math
from exercise_1 import *

class Line:
    def __init__(self, x2, y2):
        self.x1=0 
        self.y1=0
        self.x2=x2
        self.y2=y2
        self.m = (self.y2 - self.y1) / (self.x2 - self.x1)
        self.q = (self.x1 * (self.y2 - self.y1) / (self.x2 - self.x1)) + self.y1
    def line_from_point(self, point1, point2):
        self.x1=point1.x
        self.y1=point1.y
        self.x2=point2.x
        self.y2=point2.y
        self.m = (self.y2 - self.y1) / (self.x2 - self.x1)
        self.q = (self.x1 * (self.y2 - self.y1) / (self.x2 - self.x1)) + self.y1
    def distance(self, point1):
        a=1
        b=0
        c=0
        if(self.m != 0.0):
            b= -1 / self.m
        if(self.m != 0.0):
            c= self.q / self.m
        d = math.fabs((a*point1.x) + (b*point1.y) + c) / math.sqrt(a**2 + b**2)
        return d
    def intersection(self, line1):
        p = Point((line1.q - self.q)/(self.m - line1.m), ((self.m)*(line1.q - self.q)/(self.m - line1.m))+self.q)
        return p
    def __repr__(self):
        return(f"y= {self.m} x + {self.q}")

if __name__=="__main__":
    l=Line(3,2)
    print(l)

    a=Point(0,1)
    b=Point(2,2)
    l.line_from_point(a,b)
    print(l)

    l=Line(1,0)
    a=Point(1,5)
    print(l.distance(a))

    m=Line(-1, 0)
    i=l.intersection(m)
    print(i)