from Poo-python.Guiao1.Vehicle import Vehicle
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


    
class CombustVehicle(Vehicle):
    pass
print(EletricVehicle('bmw','red','43-fr-32','23',43,454,3))