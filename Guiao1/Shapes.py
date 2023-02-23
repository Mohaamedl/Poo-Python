import turtle
import math 
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
    


class Rectangle(Shapes):
    def __init__(self,color,point,sideA,sideB):
        self.sideA = sideA
        self.sideB = sideB
        super().__init__(color,point)

    def getSideA(self):
        return self.sideA
    def getSideB(self):
        return self.sideB

    def setSideA(self,A):
        self.sideA = A
    def setSideB(self,B):
        self.sideA = B
    def calArea(self):
        return self.sideA*self.sideB
    def calPer(self):
        return self.sideA*2 + self.sideB*2
    def draw(self):
        turtle.goto(self.center.getX(),self.center.getY())
        turtle.pendown()

        turtle.speed(5)
        turtle.pensize(10)
        turtle.pencolor(self.color) 
        turtle.forward(self.sideA)
        turtle.left(90)
        turtle.forward(self.sideB)
        turtle.left(90)
        turtle.forward(self.sideA)
        turtle.left(90)
        turtle.forward(self.sideB)
        turtle.penup()


class Square(Shapes):
    def __init__(self,color,center,side):
        self.side=side
        super().__init__(color,center)
    def getSide(self):
        return self.side
    def setSide(self,s):
        self.side = s
    def calArea(self):
        return self.side**2
    def calPer(self):
        return self.side*4
    def draw(self):
        turtle.goto(self.center.getX(),self.center.getY())
        turtle.pendown()

        turtle.speed(5)
        turtle.pensize(self.side/15)
        turtle.pencolor(self.color) 
        turtle.forward(self.side)
        turtle.left(90)
        turtle.forward(self.side)
        turtle.left(90)
        turtle.forward(self.side)
        turtle.left(90)
        turtle.forward(self.side)
        turtle.penup()

class Circle(Shapes):
    def __init__(self,color,center,radius:float):
        assert radius>=0, "radius must be positive number!"
        self.radius = radius
        super().__init__(color,center)
    def __str__(self):
        return f'Circle: radius = {self.radius}, center = {self.center}, color = {self.color}'
    def getRadius(self):
        return self.radius
    def setRadius(self,r):
        self.radius = r
    def calArea(self):
        return self.radius**2*math.pi
    def calPer(self):
        return 2*math.pi*self.radius
    def draw(self):
        turtle.goto(self.center.getX(),self.center.getY()) 
        turtle.pendown()
        turtle.speed(self.radius/8)
        turtle.pensize(self.radius/10)
        turtle.pencolor(self.color) 
        turtle.circle(self.radius)
        turtle.penup()
    def intersect(self,c):
        if self.center.distance(c.center)<=self.radius+c.radius:
            return True
        else:
            return False


