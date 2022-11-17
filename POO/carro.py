class Carro:
    def __init__(self, velocidade):
        self.velocidade = velocidade

    def acelerar(self):
        self.velocidade += 10

carro1 = Carro(90)
carro1.acelerar()

carro2 = Carro(80)
carro2.acelerar()

carro3  = Carro(180)
carro2.acelerar()
