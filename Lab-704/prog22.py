import math

class GeometricObject:
    def __init__(self,color,fill):
        self.color = color
        self.fill = fill

    def getArea(self):
        pass

    def getPerimeter(self):
        pass

class Triangle(GeometricObject):
    '''defines a triangle with sides ss1,s2,s3, color and fill'''
    def __init__(self,color,fill,s1=1.0,s2=1.0,s3=1.0):
        super().__init__(color,fill)
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3

    def getSides(self):
        return self.s1,self.s2,self.s3

    def getPerimeter(self):
        return self.s1 + self.s2 + self.s3

    def getArea(self):
        p = self.getPerimeter() / 2
        return round(math.sqrt(p * (p-self.s1) * (p-self.s2) * (p-self.s3)) , 2)

    def __str__(self):
        s = 'Side : '+str(self.getSides())
        s += '\nColor : '+str(self.color)
        s += '\nFill : '+str(self.fill)
        s += '\nArea : '+str(self.getArea())
        s += '\nPerimeter : '+str(self.getPerimeter())
        return s

t1 = Triangle(l);
print(t1)
