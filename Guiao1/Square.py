from Shapes import Shapes
from point import Point
import turtle
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
