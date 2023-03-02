from abc import ABC,abstractmethod
class Product(ABC):
    _id = 1
    def __init__(self,name,stock,basePrice:float):
        self._id = Product._id
        Product._id +=1
        self._name = name
        self._stock = stock
        self._basePrice = basePrice

    def __str__(self):
        return f'{self._id:-10d} {self._name:15s} {self._stock:10d} {self._basePrice:10.2f}'
    

    def getName(self):
        return self._name
    
    def getStock(self):
        return self._stock
    
    def getBasePrice(self):
        return self._basePrice
    
    
    def addStock(self,newStock):
        try:
            if newStock<=0:
                raise Exception('no negative stock')
            self._stock+=newStock
        except Exception as e:
            print(e)
    @abstractmethod
    def txPrice():
        raise NotImplementedError
    
class Book(Product):
    def __init__(self,name,stock,basePrice:float,authors=[]):
        super().__init__(name,stock,basePrice)
        self._authors = set(authors)

    def __str__(self):
        return super().__str__() + f'  {self.txPrice():5.2f}'
    
    def txPrice(self):
        return self._basePrice + self._basePrice * 0.06
    def addAuthor(self,aut):
        v = list(self._authors)
        v.append(aut)
        self._authors = set(v)


    def getAuthors(self):
        return self._authors
    

    def getNumAuthors(self):
        return len(set(self._authors))
    


class Television(Product):
    def __init__(self,brand:str,model:str,stock:int,basePrice:float,screenSize:int):
        super().__init__(str(brand+model),stock,basePrice)
        self._screenSize = screenSize

    def getScreenSize(self):
        return self._screenSize

    def txPrice(self):
        return self._basePrice + self._basePrice * 0.23
    def __str__(self):
        return super().__str__() +f'  {self.txPrice():5.2f}'
    
class Phone(Product):
    def __init__(self,branc:str,model:str,stock:int,basePrice:float):
        super().__init__(branc+model,stock,basePrice)
    def txPrice(self):
        return self._basePrice + self._basePrice * 0.23
    def __str__(self):
        return super().__str__() +f'  {self.txPrice():5.2f}'

class HomeAppliance(Product):
    def __init__(self,type:str,brand:str,model:str,stock:int,basePrice:float):
        super().__init__(type+brand+model,stock,basePrice)
        self._classe = ''

    def __str__(self):
        return super().__str__() + f'  {self.txPrice():5.2f}'
    
    def setClasse(self,newC):
        self._classe = newC
    def txPrice(self):
        return self._basePrice + self._basePrice * 0.23