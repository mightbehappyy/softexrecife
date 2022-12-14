from entidade import Entidade

class Estudante(Entidade):
    def __init__(self, nome, idade, nota):
        super().__init__(nome, idade)
        self.nota = nota
    def acao(self):
        print("Estudando")

    def getNome(self):
        return self.nome

    def setNome(self,nome):
        self.nome = nome

    def getIdade(self):
        return self.idade

    def setIdade(self, idade):
        self.idade = idade
    
    def getNota(self):
        return self.nota
    
    def setNota(self, nota):
        self.nota = nota
    
    def printidade(self):
        print("Idade", self.idade)
    
    def printnome(self):
        print("Nome", self.nome)
    
    def printnota(self):
        print("Nota", self.nota)
    