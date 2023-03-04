class Book:
    id = 99
    def __init__(self,*args):
        if len(args) ==1 :
            self.__class__.id +=1
            self.id = Book.id
            self.title = args[0]
            self.loanType = "NORMAL"
        elif len(args) == 2:
            Book.id +=1
            self.id = Book.id
            self.title = args[0]
            self.loanType = args[1]
    def __str__(self):
        return f'Book {self.id}: {self.title}, {self.loanType}'
    def getId(self):
        return self.id
    def getTitle(self):
        return self.title
    def setTitle(self,nTitle):
        self.title = nTitle
    def getLoanType(self):
        return self.loanType
    def setLoanType(self,newLoan):
        self.loanType = newLoan
class Student:
    def __init__(self,name:str,nMec:int,course:str):
        self.nMec = nMec
        self.name = name
        self.course = course
    def __str__(self):
        return f'Student: {self.nMec}; {self.name}; {self.course}'
    def getNMec(self):
        return self.nMec
    def getName(self):
        return self.name
    def getCourse(self):
        return self.course
    def setNMec(self,newN):
        self.nMec = newN
    def setCourse(self,newC):
        self.course = newC
''' 
livro1 = Book('edede','CONDICIONAL')
liv2 = Book('fsfsef')
liv3 = Book('batatas')
print(f'{livro1} \n{liv2}\n{liv3}')
s1 = Student(24234,'blabla','bliblibli')
s2 =  Student(67238,'fifi','gigigigigi')
print(f'{s1}\n{s2}')'''
def main():
    livro1= Book("Java 8", "CONDICIONAL");
    print(livro1)
    catalogo=[]
    catalogo.append(livro1)
    catalogo.append(Book("POO em Java 8"))
    catalogo.append(Book("Java para totós", "NORMAL"))
    
    print(f"ID = {catalogo[1].getId()} Título = { catalogo[1].getTitle()}")
    catalogo[2].setLoanType("CONDICIONAL")
    for livro in catalogo:
        print(livro)
    # Students
    utilizadores=[]
    utilizadores.append(Student("Catarina Marques", 80232, "MIEGI"))
    utilizadores.append(Student("Joao Silva", 90123, "Lic Física"))
    utilizadores[1].setNMec(80123)
    utilizadores.append(Student("António Costa", 100123, "Lic Matemática"))
    for aluno in utilizadores:
        print(aluno)
main()
