import random
import turtle
import math
from Guiao1.point import Point
from abc import  abstractmethod, ABC
class Figure(ABC):
    def __init__(self,color='red',center=Point(0,0)):
        self.color = color
        self.center = center
    def __str__(self) :
        return f'Circle: center = {self.center}, color = {self.color}, '
    def getCenter(self):
        return self.center
    def setCenter(self,c):
        self.center = c
    def getColor(self):
        return self.color
    def setColor(self,col):
        self.color = col
    @abstractmethod
    def calArea(self):
        raise NotImplementedError
    @abstractmethod
    def calPer(self):
        raise NotImplementedError
    @abstractmethod
    def draw(self):
        print("Figure not defined.")

class Rectangle(Figure):
    def __init__(self,color='red',center=Point(0,0),sideA=500,sideB=200):
        super().__init__(color,center)
        self.sideA = sideA
        self.sideB = sideB
    def __str__(self):
        return super(Rectangle,self).__str__() +f'side A = {self.sideA}, side B = {self.sideB}'
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
        turtle.penup()
        turtle.speed(5)
        turtle.pensize(10)
        turtle.pencolor(self.color) 
        x = self.center.getX()
        y = self.center.getY()
        x -= self.sideA / 2 #trocar dependendo da orientação
        y -= self.sideB / 2
        turtle.goto(x, y) 
        turtle.pendown()
        turtle.forward(self.sideA)
        turtle.left(90)
        turtle.forward(self.sideB)
        turtle.left(90)
        turtle.forward(self.sideA)
        turtle.left(90)
        turtle.forward(self.sideB)
        turtle.setheading(0)# resetar orientação
        turtle.penup()

class Square(Figure):
    def __init__(self,color='blue',center=Point(0,0),side=600):
        super().__init__(color,center)
        self.side = side
        
    def getSide(self):
        return self.side
    def setSide(self,s):
        self.side = s
    def calArea(self):
        return self.side**2
    def calPer(self):
        return self.side*4
    def draw(self):
        turtle.penup()
        turtle.speed(5)
        turtle.pensize(10)
        turtle.pencolor(self.color)
        x = self.center.getX()
        y = self.center.getY()
        x -= self.side / 2
        y += self.side / 2
        turtle.goto(x, y)
        turtle.pendown()

        for i in range(4):
            turtle.forward(self.side)
            turtle.right(90)
        turtle.setheading(0)# resetar orientação
        turtle.penup()

class Circle(Figure):
    def __init__(self,*args):
        if len(args)==3:
            self.radius = args[2]
            super().__init__(args[0],args[1])
        elif len(args) == 0:
            self.radius = 300
            super().__init__()
    def __str__(self):
        return f'Circle: center = {self.center}, color = {self.color}, radius = {self.radius}'
    def getRadius(self):
        return self.radius
    def setRadius(self,r):
        self.radius = r
    def calArea(self):
        return self.radius**2*math.pi
    def calPer(self):
        return 2*math.pi*self.radius
    def draw(self):
        turtle.pencolor(self.color)
        turtle.penup()
        turtle.goto(self.center.getX(),self.center.getY())
        turtle.right(90)
        turtle.forward(self.radius)
        turtle.left(90)
        turtle.pendown()
        turtle.circle(self.radius)
        turtle.penup()
        turtle.right(-90)
        turtle.forward(self.radius)
        turtle.setheading(0)# resetar orientação
        turtle.penup()
       
    def intersect(self,c):
        if self.center.distance(c.center)<=self.radius+c.radius:
            return True
        else:
            return False
class Triangle(Figure):
    def __init__(self,color='blue',center=Point(0,0),sideA=5,sideB=4,sideC=3):
        try:
            if sideA+sideB < sideC or sideA+sideC < sideB or sideC+sideB < sideA:
                raise Exception('Error, Triangle')
            super().__init__(color,center)
            self.sideA = sideA
            self.sideB = sideB
            self.sideC = sideC
        except Exception as e:
            print(e)
    def calPer(self):
        return self.sideA+self.sideB+self.sideC
    def calArea(self):
        angleAB = Triangle.angle(self.sideA, self.sideB, self.sideC)
        return 1/2 * self.sideA * self.sideB *math.sin(angleAB)
    def angle(side1, side2, side3):
        return math.degrees(math.acos((side3**2 - side2**2 - side1**2) /(-2.0 * side1 * side2)))
    def draw(self):
        angleAB = Triangle.angle(self.sideA, self.sideB, self.sideC)
        angleBC = Triangle.angle(self.sideB, self.sideC, self.sideA)
        angleCA = Triangle.angle(self.sideC, self.sideA, self.sideB)
        print(angleAB,angleBC,angleCA)
        turtle.pencolor(self.color)
        turtle.pensize(6)
        turtle.penup()
        turtle.goto(-self.sideA/2+self.center.getX(),-self.sideA/2+self.center.getY()) #uma tentativa de centralizar o triangulo sem muito trabalho
        turtle.pendown()
        turtle.forward(self.sideA)
        turtle.left(180-angleAB)
        turtle.forward(self.sideB)
        turtle.left(180-angleBC)
        turtle.forward(self.sideC)
        turtle.setheading(0)# resetar orientação
        turtle.penup()
        

class Fig:
    def random_shape():
        rn = random.randrange(0,3) 
        f=Triangle()
        if rn == 0:
            f=Circle()
        elif rn ==1:
            f= Square()
        elif rn ==2:
            f = Rectangle()
        return f
def main():
    figures = []
    for i in range(9):
        figures.append(Fig.random_shape()) # adicionar à lista figuras (círculos, quadrados…)
    for fig in figures:
        print(fig.calArea())
    turtle.setup(1000,800)
    t = Triangle('black',Point(0,0),500,500,500)
    s = Square()
    r = Rectangle()
    c = Circle()
    c1 = Circle('red',Point(-130,0),40)
    c2 = Circle('red',Point(130,0),40)
    s.draw()
    r.draw()
    c.draw()
    c1.draw()
    c2.draw()
    t.draw()
    turtle.getscreen()._root.mainloop()

#main()