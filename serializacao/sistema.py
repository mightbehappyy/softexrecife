import pickle
class Sistema():
    def __init__(self, nome, arquitetura, dono):
        self.nome = nome
        self.arquitetura = arquitetura
        self.dono = dono
    def inicializar(self):
        print(f"Inicializando {self.nome} {self.arquitetura} produzido pela {self.dono} ")

sistema1 = Sistema("Windows", "64 bits", "Microsoft")
pickle_out = open("sistema", "wb")   # comentar o pickle_in antes de executar esse codigo
pickle.dump(sistema1, pickle_out)
pickle_out.close()

pickle_in = open("sistema.txt", "rb") # comentar o pickle_out antes de descomentar este e rodar o codigo, verifique se o arquivo
carregar = pickle.load(pickle_in)     # "sistema.txt" existe
