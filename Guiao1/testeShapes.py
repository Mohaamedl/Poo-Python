from Shapes import *
from point import Point
circle = Circle('red',Point(1,1),200)
circle2 = Circle('purple',Point(250,100),250)
square = Square('blue',Point(80,80),200)
rectangle = Rectangle('green',Point(5,50),200,300)
circle.draw()
square.draw()
rectangle.draw()
circle2.draw()
c = circle.intersect(circle2)
print(f'the {circle}'+ (' not' if not c else ' ')+f' intersect the {circle2}')
# falta o metodo __str__ para retangulo e quadrado mas isso é trivial entao ignora-se