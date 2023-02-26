from Shapes import *
from point import Point
def main():
    turtle.screensize(1200,800,'black')
    turtle.setup(1200,700,)
    circle = Circle('red',Point(0,100),60)
    circle2 = Circle('purple',Point(0,-50),90)
    square = Square('blue',Point(0,0),440)
    rectangle = Rectangle('green',Point(0,50),70,90)
    circle.draw()
    square.draw()
    rectangle.draw()
    circle2.draw()
    
    c = circle.intersect(circle2)
    print(f'the {circle}'+ (' not' if not c else ' ')+f' intersect the {circle2}')
    print(circle,square,rectangle)
    circle3 = Circle('black',Point(0,-100),0)
    for i in range(100,0,-4):
        circle3.setRadius(i)
        circle3.draw()
    turtle.getscreen()._root.mainloop()
main()