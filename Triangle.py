from math import acos, degrees
class Triangle:

    def __init__(self, a = 3, b = 4, c = 5): #default values
        self.A = a
        self.B = b
        self.C = c

    def getSides(self):
        return "Length of A: " + str(self.A) + ", Length of B: " + str(self.B) + ", Length of C: " + str(self.C)
    
    def getAlpha(self): #law of cosines
        self.Alpha = (self.B ** 2 + self.C ** 2 - self.A ** 2)/(2*self.B*self.C)
        return degrees(acos(self.Alpha))

    def __str__(self):
        return self.getSides()
    
class Quadrangle(Triangle):

    def __init__(self, a = 3, b = 4, c = 5, d = 6): #default values
        self.D = d
        super().__init__(a, b, c)

    def getSides(self):
        return super().getSides() + ", Length of D: " + str(self.D)

    def __str__(self):
        return self.getSides()

        
myTriangle = Triangle()
print(myTriangle) #calls __str__ method by default
print("Angle of alpha:\t", myTriangle.getAlpha())
myOtherTriangle = Triangle(6,8,10)
print(myOtherTriangle)
myThirdTriangle = Triangle(a = 2, c = 6) #b is default value of 4
print(myThirdTriangle)
myQuadrangle = Quadrangle(1,2,3,4)
print(myQuadrangle)

