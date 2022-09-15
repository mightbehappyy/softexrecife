def terrestre():
    pterrestre1 = str(input("Cabe apenas uma pessoa?"))
    if pterrestre1 == "Sim":
        pterrestre2 = str(input("É pesado?"))
        if pterrestre2 == "Sim":
            print("Então, o transporte escolhido foi um trator")
        else:
            pterrestre3 = str(input("Tem pedal?"))
            if pterrestre3 == "Sim":
                print("Então, o transporte escolhido foi uma bicleta")
    else:
        capacete = str(input("Usa capacete?"))
        if capacete == "Sim":
            print("Então, o transporte escolhido foi uma moto")
        if capacete == "Não":
            print("Então o seu transporte tem passsageios")
            trilho = str(input("Usa trilho?"))
            if trilho == "Sim":
                print("Então, o transporte escolhido foi um trem")
            else:
                print("Então o transporte anda na pista")
                print("O seu transporte pode ser alto ou leve")
                alto = str(input("O transporte é alto?"))
                if alto == "Sim":
                    print("O transporte pode ter uma carroceria ou cobrador")
                    carroceria = str(input("Usa carroceria?"))
                    if carroceria == "Sim":
                        print("Então o seu transporte é um caminhão")
                    else:
                        print("O seu transporte tem cobrador, logo é um onibus")
                else: 
                    print("Seu transporte é leve logo é um carro")



def aereo():
    print("Seu tranporte é aereo")
    print("Seu transporte pode precisar pular ou permite que você viage dentro")
    pular = input("Precisa pular?")
    if pular == "Sim":
        print("Então seu transporte é uma asa delta")
    else:
        print("Então você pode viajar entro.")
        print("O seu transporte pode ser devagar ou ter um piloto")
        devagar = input("É devagar?")
        if devagar == "Sim":
            print("Então seu transporte é um balão")
        else:
            print("Então tem piloto")
            print("Seu transporte pode possuir asas fixas ou fazer voo vertical")
            asafixa = input("Ele possui asas fixas?")
            if asafixa == "Sim":
                print("Então seu transporte é o avião")
            else:
                print("Então seu transporte é um helicóptero")            
    
def aquatico():
    agua = input("Seu transporte fica coberto por água?")
    if agua == "Sim":
        print("Seu transporte é um submarino")
    else:
        vela = input("O seu veiculo possui vela?")
        if vela == "Sim":
            print("Seu veiculo é um barco")
        else:
            motor = input("Seu veiculo tem motor?")
            if motor == "Sim":
                alto = input("Seu veiculo é alto?")
                if alto == "Sim":
                    print("Seu transporte é um navio")
                if alto == "Não":
                    descoberto = input("O seu veiculo pode ser descoberto?")
                    if descoberto == "Sim":
                        print("Então seu veiculo é uma lancha")

def principal():
    print("Pense em um dos seguintes transportes, o programa vai adivinhar em que transporte você está pensando")
    print("-Trator\n"
"-Moto.\n"
"-Bicicleta \n" 
"-Trem\n"
"- Carro\n"
"- Caminhão \n"
"- Ônibus\n"
"- Paraquedas\n"
"- Balão \n"
"- Avião \n"
"- Helicóptero \n"
"- Submarino \n"
"- Barco \n"
"- Navio \n"
"- Lancha\n"
)
    p1 = str(input("É terrestre?"))
    if p1 == "Sim":
        terrestre()
    if p1 == "Não":
        p2 = str(input("É aéreo?"))
        if p2 == "Sim":
            aereo()
        if p2 == "Não":
            print("Então seu transporte é aquático")
            aquatico()
principal()
