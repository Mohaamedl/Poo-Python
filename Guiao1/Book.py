class Book:
    id = 100
    def __init__(self,title:str,loanType:str):
        self.title = title
        self.id = self.id+1
        self.loanType = loanType
    def __init__(self,title:str):
        self.title = title
        self.id = self.id+1
        self.loanType = 'NORMAL'
        
    def __str__(self):
        return f'Book {self.id}: {self.title}, {self.loanType}'
    def getId(self):
        return self.Id
    
    
livro1 = Book('edede','dede')
liv2 = Book('fsfsef')
print(f'{livro1} \n {liv2}')