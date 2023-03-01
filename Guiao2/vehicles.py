from Guiao1.vehicle import Vehicle

class ElectricVehicle(Vehicle):
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
    def setPotency(self,p):
        self.potency = p
    def setNumEngines(self,nE):
        self.numEngines = nE

    


    
class CombustionVehicle(Vehicle):
    def __init__(self,brand:str,color:str,plateNum:str,
                  max_speed:float, kilometers:float,cc:float):
        try: 
            if cc<=0:
                raise Exception('Error in args')
            super().__init__(brand,color,plateNum, max_speed, kilometers)
            self.cc = cc
        except Exception as e:
            print(e)
    def __str__(self):
        return super().__str__() + f', {self.cc} CC'
print(ElectricVehicle('bmw','red','gt-89-32',23,43,454,3))
v1 = ElectricVehicle('Tesla','black','DZ-59-27',190,0,100,1)
v2 = CombustionVehicle('Ferrari','red','OF-00-00',310,0,3000)
print( v1)
print(v2)
