import random
import turtle
from Guiao1.Shapes import *
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

if __name__=='__main__':
    main()