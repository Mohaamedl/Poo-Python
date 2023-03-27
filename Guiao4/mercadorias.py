class Mercadoria:
    def __init__(self,nome,peso,empresa):
        self._nome = nome
        self._peso = peso
        self._empresa = empresa
        
    def __str__(self):
        return f''