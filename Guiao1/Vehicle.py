class Vehicle:
    def __init__(self, max_speed, kilometers):
        self.max_speed=max_speed
        self.kilometers = kilometers
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