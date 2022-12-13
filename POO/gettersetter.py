class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def nomeGet(self):
        return self.nome

    def nomeSet(self, nome):
        self.nome = nome
    
    def idadeGet(self):
        return self.idade

    def idadeSet(self, idade):
        self.idade = idade
