from Shapes import Shapes
import turtle
from point import Point
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

