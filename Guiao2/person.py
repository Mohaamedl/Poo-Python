class Person:
    ''' Simple class for a person'''

    def __init__(self,name, id, birth_date):
        '''Class constructor, with parameters: name,  identification document (id), and birth data''' 
        self.__name = name
        self.__id = id
        self.__birth = birth_date
        
    def __str__ (self):
        '''Return a string representation of the information abouth the person'''
        return f"{self.__name}, ID {self.__id}, born {self.__birth}"


    # setters --------------------
    
    # NOTE: not often but people change names (ex: marriage)
    def set_name(self, new_name):
        '''Method to alter the name to new_name'''
        self.__name = new_name

    def set_id(self, new_id):
        '''Method to alter identification (id) to new_id'''
        self.__id = new_id

    # NOTE: no setters for birth_date (does not make sense)  

    # getters --------------------
    def get_name(self):
        '''Method to get the name of the person'''
        return self.__name
    
    def get_id(self):
        '''Method to get the id of the person'''
        return self.__id
    
    def get_birth_date(self):
        '''Method to get the date of birth of the person'''
        return self.__birth

def test():
    p1 = Person("Mary Wilson",123456,"22/03/1985")
    print(p1)

    print(f"{p1.get_name()} - {p1.get_id()} - {p1.get_birth_date()}")

    p1.set_name("Mary Wilson Smith") # by marriage
    p1.set_id("CC 23456") # new id
    print(p1)


if __name__ == "__main__":
    test()
    


    