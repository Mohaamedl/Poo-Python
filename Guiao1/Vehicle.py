import re
class Vehicle:
    def __init__(self,brand:str,color:str,plateNum:str, max_speed:float, kilometers:float):
        try:
            if  max_speed<0 or kilometers<0 or re.search('[a-zA-Z]{2}-[0-9]{2}-[0-9]{2}',plateNum)==None:
                raise Exception('Enter valid values please.')
            self.max_speed=max_speed
            self.kilometers = kilometers
            self.color = color
            self.brand = brand
            self.plateNum = plateNum
        except Exception as exc:
            print(exc)

    def __str__(self):
        return f'{self.plateNum} : {self.brand}, {self.color}, {self.max_speed} km/h, {self.kilometers} km'
    def set_max_speed(self, max_sp): 
        self.max_speed=max_sp
    def get_max_speed(self):# returns value of max_speed attribute 
        return self.max_speed  
    def set_kilometers(self, kms): 
        self.kilometers= kms
    def get_kilometers(self):# returns value of kilometers attribute 
        return self.kilometers





















'''modelX = Vehicle(240, 18) 

print(modelX.max_speed, modelX.kilometers) 
modelX.set_kilometers(1000) 
modelX.set_max_speed(200) 
print(f"Vehicle has {modelX.kilometers} Km and a max speed of {modelX.max_speed} Kms/h") '''