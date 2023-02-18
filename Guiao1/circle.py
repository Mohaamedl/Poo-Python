from point import Point
from Shapes import Shapes
import math
import turtle
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

