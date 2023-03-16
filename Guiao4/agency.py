
class Agency:
    
    def __init__(self,name:str,address:str,listAccommodation = [],listVehicles = []):
        self._name = name
        self._address = address
        self._listAccommodation = listAccommodation
        self._listVehicles = listVehicles

    def __str__(self):
        pass



    def addAccomodation(self.acc):
        pass











def test():
    ap = Apartment('grande hotel 5estrelas','ali algures',997.07,5,2,True)
    print(ap)
    ap.checkOut()
    print(ap)
    ap.checkIn()
    print(ap)
    ap.checkIn()
    print(ap)
    ap2 =  Apartment('grande 5estrelas','ali algures',997.07,5,2,True)
    print(ap2)
    r = Room('patati','patata',98,5,'single')
    print(r)
    r2 =  Room('bom','sitio',98,5,'twin',False)
    print(r2)


if __name__ == '__main__':
    test()