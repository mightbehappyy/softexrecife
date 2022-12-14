from entidade import Entidade


class Professor(Entidade):
    def __init__(self, nome, idade, materia):
        super().__init__(nome, idade)
        self.materia = materia
    def acao(self):
        print("Corrigindo provas") 

    def getNome(self):
        return self.nome

    def setNome(self,nome):
        self.nome = nome

    def getIdade(self):
        return self.idade

    def setIdade(self, idade):
        self.idade = idade
    
    def getMateria(self):
        return self.materia
    
    def setMateria(self, materia):
        self.materia = materia

    def printidade(self):
        print("Idade", self.idade)
    
    def printnome(self):
        print("Nome", self.nome)
    
    def printmateria(self):
        print("Materia", self.materia)