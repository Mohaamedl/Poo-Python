from Guiao1.vehicle import Vehicle

class EletricVehicle(Vehicle):
    def __init__(self,brand:str,color:str,plateNum:str,
                  max_speed:float, kilometers:float,potency:float,numEngines:int):
        try: 
            if potency<0 or numEngines<=0:
                raise Exception('Error in args')
            super().__init__(brand,color,plateNum, max_speed, kilometers)
            self.potency = potency
            self.numEngines = numEngines
        except Exception as e:
            print(e)
    def __str__(self):
        return super().__str__()+ f', {self.numEngines} '+("motors" if self.numEngines>1 else " motor")+f', {self.potency} Kw'
    def getPotency(self):
        return self.potency
    def getnumEngines(self):
        return self.numEngines
    


    
class CombustVehicle(Vehicle):
    pass
print(EletricVehicle('bmw','red','gt-89-32',23,43,454,3))
