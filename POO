class Carro():
    def __init__(self, marca, modelo, potencia, status):
        self.marca = marca
        self.modelo = modelo
        self.potencia = potencia
        self.status = status
    def ligar(self):
        self.status = True 
        print("Ligando carro...")
    def Acelerar():
        print("Acelerando")
    def desligar(self):
        self.status = False
        print("Desligando carro...")


class Caneta():
    def __init__(self, cor, marca, carga, tampa):
        self.cor = cor
        self.marca = marca
        self.carga = carga
        self.tampa = tampa
    def escrever(self):
        print("Escrevendo...")
        self.carga = self.carga - 5
    def destampar(self):
        self.tampa = False
        print("Destampando...")
        if self.tampa == False:
            self.tampa = True
            print("Tampando...")
    def recarregar(self):
        print("Recarregando")
        self.carga = 100



class Tenis():
    def __init__(self, tipo, pessoas, tempo, status):
        self.tipo = tipo
        self.pessoas = pessoas
        self.tempo = tempo
        self.status = status
    def acabar(self):
        self.status = "Encerrada"
        print("Encerrando partida")
    def comecar(self):
        print("Começar partida")
        self.status = "Em andamento"
    def cancelar(self):
        self.status = "Cancelada"
        print("Cancelada")


class Clima():
    def __init__(self, temp, umidade, probchuva, chovendo):
        self.temp = temp
        self.umidade = umidade
        self.probchuva = probchuva
        self.chovendo = chovendo
        
    def aumentartemp(self):
        self.aumentartemp = self.aumentartemp + 5
    def chover(self):
        self.chuva = True
    def aumentarumi(self):
        self.aumentarumi = self.aumentarumi + 5

novaPartida = Tenis("Casual", 4, 90, "Em andamento")
novaCaneta = Caneta("Vermelha", "Bic", 50, True)
novoCarro = Carro("Bmw","e30", 200, False)
novoClima = Clima(25, 89, 50, False)
