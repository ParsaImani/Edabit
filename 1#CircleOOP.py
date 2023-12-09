import math

PI=math.pi

class Circle:
    
    def __init__(self,r):
        self.r=r

    def getArea(self):
        
        return PI*(self.r)**2
    
    def getPerimeter(self):

        return PI*2*(self.r)

