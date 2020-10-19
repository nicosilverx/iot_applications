import math

class SquareManager:
    def __init__(self, side):
        self.side = side
        self.area = side*side
        self.perimeter = side * 4
        self.diagonal = math.sqrt(2) * side

if __name__=="__main__":
    sm=SquareManager(3)
    print(f"The area of the square with side {sm.side} = {sm.area}")
    print(f"The perimeter of the square with side {sm.side} = {sm.perimeter}")
    print(f"The diagonal of the square with side {sm.side} = {sm.diagonal}")
