from point import Point
class Shapes:
    def __init__(self,color:str,center:Point):
        self.color = color
        self.center = center
    def getCenter(self):
        return self.center
    def setCenter(self,c):
        self.center = c
    def getColor(self):
        return self.color
    def setColor(self,col):
        self.color = col
    
