from abc import ABC,abstractmethod
class Product(ABC):
    __id = 1
    def __init__(self,name,stock,basePrice:float):
        self.__id = Product.id
        Product.__id +=1
        self.__name = name
        self.__stock = stock
        self.__basePrice = basePrice
    def __str__(self):
        return f'Abstarct product'
    def addStock(self,newStock):
        try:
            if newStock<=0:
                raise Exception('no negative stock')
            self.stock+=newStock
        except Exception as e:
            print(e)
        

