import sys

class TriangleError(RuntimeError):
    def printError(self):
        print('Sum of any 2 sides of a triangle must be greater than the 3rd side')
        sys.exit()

class GeometricObject:
    def __init__(self,color,fill):
        self.color = color
        self.fill = fill

    def getColor(self):
        return self.color

    def getFill(self):
        return self.fill

class Triangle(GeometricObject):
    '''defines a triangle with sides ss1,s2,s3, color and fill'''
    def __init__(self,color,fill,s1,s2,s3):
        super().__init__(color,fill)
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
        try:
            if self.s1 + self.s2 <= self.s3 or self.s1 + self.s3 <= self.s2 or self.s2 + self.s3 <= self.s1:
                raise TriangleError
            else:
                pass
        except TriangleError as e:
            e.printError()

    def getSides(self):
        return [self.s1,self.s2,self.s3]

    def getPerimeter(self):
        return self.s1 + self.s2 + self.s3

    def getArea(self):
        s = self.getPerimeter() / 2
        return (s * (s-self.s1) * (s-self.s2) * (s-self.s3) )**0.5

    def __str__(self):
        s = 'Side : '+str(self.getSides())
        s += '\nColor : '+str(self.color)
        s += '\nFill : '+str(self.fill)
        s += '\nArea : '+str(self.getArea())
        s += '\nPerimeter : '+str(self.getPerimeter())
        return s

def main():
    t1 = Triangle('green',True,4,5,6)
    print(t1)

main()
