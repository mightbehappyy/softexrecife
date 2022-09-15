from random import randint
rodas = int(input("Quantas rodas o veiculo tem?"))
peso = int(input("Qual é o peso do veículo"))
pessoas = int(input("Quantas pessoas esse veículo acomoda?"))

if rodas == 2 or rodas == 3:
    print("Habilitação tipo A")
if rodas == 4 and pessoas <= 8 and peso <= 3500:
    print("Habilitação tipo B")
if rodas >= 4 :
    if 3500 <= peso <= 6000:
        print("Habilitação tipo C")
    elif pessoas > 8:
        print("Habilitação tipo D")
    elif peso > 8000:
        print("Habilitação tipo E")
else:
    print("Veículo inválido")
    
