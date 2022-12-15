import pickle
class Sistema():
    def __init__(self, nome, arquitetura, dono):
        self.nome = nome
        self.arquitetura = arquitetura
        self.dono = dono
    def inicializar(self):
        print(f"Inicializando {self.nome} {self.arquitetura} produzido pela {self.dono} ")

sistema1 = Sistema("Windows", "64 bits", "Microsoft")
pickle_out = open("sistema", "wb")   # COMENTAR O PICKLE_IN ANTES DE EXECUTAR ESSE CODIGO
pickle.dump(sistema1, pickle_out)
pickle_out.close()



pickle_in = open("sistema.txt", "rb") # COMENTAR O PICKLE_OUT ANTES DE DESCOMENTAR ESTE E RODAR O CODIGO, VERIFIQUE SE O ARQUIVO
carregar = pickle.load(pickle_in)     # "SISTEMA.TXT" EXISTE
print(carregar)
