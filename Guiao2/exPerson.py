import names
import random
class Person:
    ''' Simple class for a person'''

    def __init__(self,name, id, birth_date):
        '''Class constructor, with parameters: name,  identification document (id), and birth data''' 
        self._name = name
        self._id = id
        self._birth = birth_date
        
    def __str__ (self):
        '''Return a string representation of the information abouth the person'''
        return f"{self._name}, ID {self._id}, born {self._birth}"


    # setters --------------------
    
    # NOTE: not often but people change names (ex: marriage)
    def setName(self, new_name):
        '''Method to alter the name to new_name'''
        self._name = new_name

    def setId(self, new_id):
        '''Method to alter identification (id) to new_id'''
        
        self._id = str(''.join([x for x in new_id.split() if x.isdigit()]))

    # NOTE: no setters for birth_date (does not make sense)  

    # getters --------------------
    def getName(self):
        '''Method to get the name of the person'''
        return self._name
    
    def getId(self):
        '''Method to get the id of the person'''
        return self._id
    
    def getBirthDate(self):
        '''Method to get the date of birth of the person'''
        return self._birth

class Student(Person):
    def __init__(self,name,id,birthDate,course,nMec):
        super().__init__(name,id,birthDate)
        self._course = course
        self._nMec = nMec
    def __str__(self):
        return super().__str__() + f', course: {self._course}, MecNumbr: {self._nMec}'
    def getCourse(self):
        return self._course
    def getNMec(self):
        return self._nMec
    def setCourse(self,newC):
        self._course = newC
class Professor(Person):
    def __init__(self,name,id,birthDate,ucs=[]):
        super().__init__(name,id,birthDate)
        self._ucs = set(ucs)
    def __str__(self):
        return super().__str__() + f', UCs: {self._ucs}'
    def getUcs(self):
        return self._ucs
    def addUcs(self,uc):
        s = list(self._ucs)
        s.append(uc)
        self._ucs = set(s)






def test():
    p1 = Person("Mary Wilson",123456,"22/03/1985")
    print(p1)
    print(f"{p1.getName()} - {p1.getId()} - {p1.getBirthDate()}")
    p1.setName("Mary Wilson Smith") # by marriage
    p1.setId("CC 23456") # new id
    print(p1)
    ucss = ['ALGA','CI','CII','CIII','TFE','FMOD','SM','IP','PA','POO','FC']
    students = []
    profs = []
    for i in range(30):
        if i <25:
            students.append(Student(names.get_full_name(),
                                    random.randint(100000,9999999),
                                    str(random.randint(1,31))+'-'+str(random.randint(1,12))+'-'+str(random.randint(1950,2005)),
                                    'Fisica',random.randint(10000,900000)))
        else:
            profs.append(Professor(names.get_full_name(),
                                    random.randint(100000,99999999),
                                    str(random.randint(1,31))+'-'+str(random.randint(1,12))+'-'+str(random.randint(1950,2005)),
                                    random.choices(ucss,k=random.randint(1,11))))
    classe = []
    classe.extend(profs)
    classe.extend(students)
    for p in classe:
        print(p)

if __name__ == "__main__":
    test()
    


    