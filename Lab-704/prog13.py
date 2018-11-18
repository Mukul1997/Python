class Rectangle:
    def __init__(self,height=2,width=1):
        self.height = height
        self.width = width

    def getPerimeter(self):
        return 2 * (self.width + self.height)

    def getArea(self):
        return self.width * self.height

r1 = Rectangle()
r2 = Rectangle(3,4)

print("P1 : ",r1.getPerimeter())
print("A1 : ",r1.getArea())

print("P2 : ",r2.getPerimeter())
print("A2 : ",r2.getArea())
