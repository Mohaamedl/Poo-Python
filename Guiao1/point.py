import random
import math
import time
class Point:
    def __init__(self,x:float,y:float):
        self.x = x
        self.y = y
    def __str__(self):
        return f'({self.x},{self.y})'
    def setX(self,xx):
        self.x = xx
    def setY(self,yy):
        self.y = yy
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def distance(self,p2):
        return math.sqrt((self.x-p2.x)**2 + (self.y-p2.y)**2)

"""
ti = time.time()
p1 = Point(4.8654,8.9004)
p2 = Point(2.5308,94.964076)
print(fr'the distance between {p1} and {p2} is : {p1.distance(p2):.2f}') #teste inicial
points=[]
points.append(p1) #so para reutilizar
points.append(p2) 
#teste extensivo
for i in range(10):#pode ser qlqr valor q se deseja criar de pontos
    x = round(random.randint(1,89)*math.pi,2) #pode-se por (-1)**randind(1,20) por exemplo para incluir numeros negativos tambem
    y = round(random.randint(1,89)*math.pi,2)
    p1 = Point(x,y)
    print(p1)
    points.append(p1)
for point in points:
    newpts = points.copy()
    newpts.remove(point)
    for p in newpts:
        print(f'the distance between {point} and {p} is : {point.distance(p):.2f}')
tf = time.time()
t = tf-ti 
print(f'Este algoritmo levou {t} segundos a ser executado.')
"""