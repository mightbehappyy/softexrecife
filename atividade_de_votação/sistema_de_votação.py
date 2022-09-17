import enum
from ssl import _create_unverified_context
maior = 0
sair = False
voto = ""
class candidatos(enum.Enum):
    candidato_x = 0
    candidato_y = 0
    candidato_z = 0
    branco = 0
    nulo = 0
candidato_x = candidatos.candidato_x.value 
candidato_y = candidatos.candidato_y.value 
candidato_z = candidatos.candidato_z.value 
branco = candidatos.branco.value 
nulo = candidatos.nulo.value

while sair != True:
    try:
        voto = int(input("Digite seu voto"))

        if voto == 899:
            candidato_x += 1
        elif voto == 847:
            candidato_y += 1
        elif voto == 515:
            candidato_z += 1
        elif voto == 0:
            branco += 1
        else:
            nulo += 1
        sair = input("Sair?")
        if sair == "Sim":
            sair = True
            print(f"Fim da votação\nCandidato X teve {candidato_x} votos\nCandidato Y teve {candidato_y} " 
            f"votos\nCandidato Z teve {candidato_z} votos\nHouveram {branco} votos em branco e {nulo} nulos")
            if candidato_x > candidato_y and candidato_x > candidato_z:
                print("O candidato X é o vencedor")
            elif candidato_y > candidato_x and candidato_y > candidato_z:
                print("Candidato Y é o vencedor")
            elif candidato_z > candidato_x and candidato_z > candidato_y:
                print("Candidato Z é o vencedor")
            else:
                if candidato_x == candidato_y and candidato_y == candidato_z and candidato_x == candidato_z:
                    print("Todos os candidatos emparatam, haverá uma nova eleição")
                elif candidato_x == candidato_y:
                    print("Candidato X e Y vão para o segundo turno")
                elif candidato_x == candidato_z:
                    print("Candidato X e Z vão para o segundo turno")
                elif candidato_y == candidato_z:
                    print("Candidato Y e Z vão para o segundo turno")
        else:
            sair = False
    except:
        print("Insira um caractere adequado")
        
