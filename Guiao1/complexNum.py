class Complex:
    def __init__(self,real:float,imaginary:float):
        """Initialize Complex class's attributes."""        
        self.real = real 
        self.imaginary = imaginary
    def __repr__(self):
        """Return string representation"""
        if self.imaginary==0:
            return (f'{self.real}' )
        elif self.real==0:
            return ((''if self.imaginary >= 0 else' - ') +f'{abs(self.imaginary)}i')
        return (f'({self.real}' +  (' + 'if self.imaginary >= 0 else' - ') + f'{abs(self.imaginary)}i)')
    def __str__(self):
        if self.imaginary==0:
            return (f'{self.real}' )
        elif self.real==0:
            return ((''if self.imaginary >= 0 else' - ') +f'{abs(self.imaginary)}i')
        return (f'({self.real}' +  (' + 'if self.imaginary >= 0 else' - ') + f'{abs(self.imaginary)}i)')
    def add(self,complex):
        zr= self.real+complex.real
        zi= self.imaginary+complex.imaginary
        nZ = Complex(zr,zi)
        return nZ.__repr__()
    def subtract(self,complex):
        zr= self.real-complex.real
        zi= self.imaginary-complex.imaginary
        nZ = Complex(zr,zi)
        return nZ.__repr__()
    def multiply(self,z):
        re = z.real*self.real-z.imaginary*self.imaginary
        im = z.real*self.imaginary+z.imaginary*self.real
        nZ = Complex(re,im)
        return nZ.__repr__()

cmplx1= Complex(1,1)
cmplx2= Complex(2,2)
cmplx3 = Complex(1,-1)
print(cmplx1)
print(cmplx2)
print(cmplx1.add(cmplx2))
print(cmplx1.subtract(cmplx2))
print(f"{cmplx1} + {cmplx2}  = {cmplx1.add(cmplx2)}")
print(f"{cmplx2} + {cmplx1}  = {cmplx2.add(cmplx1)}")
print(f"{cmplx2} - {cmplx1}  = {cmplx2.subtract(cmplx1)}")
print(f"{cmplx2} x {cmplx1}  = {cmplx2.multiply(cmplx1)}")
print(cmplx3)
print(cmplx3.multiply(cmplx1))
print(cmplx3.__str__())
