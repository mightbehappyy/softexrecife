from xml.dom.minidom import Notation
import pandas as pd
banco_de_dados = pd.read_csv("tabela.csv", delimiter=";", index_col=0)

aprovadosA  = 0
maiornotaA = 0
aprovadosB = 0
maiornotaB = 0
aprovadosC  = 0
maiornotaC = 0
aprovadosD = 0
maiornotaD = 0
maiornotageral = 0
nomemaiornota = ""
turmamaiornota = ""

for nota in banco_de_dados.itertuples():
    if nota[2] == "A":
        if nota[1] > 7.0:
            aprovadosA += 1
        if nota[1] > maiornotaA:
            maiornotaA = nota[1]
    if nota[2] == "B":
        if nota[1] > 7.0:
            aprovadosB += 1
        if nota[1] > maiornotaB:
            maiornotaB = nota[1]
    if nota[2] == "C":
        if nota[1] > 7.0:
            aprovadosC += 1
        if nota[1] > maiornotaC:
            maiornotaC = nota[1]
    if nota[2] == "D":
        if nota[1] > 7.0:
            aprovadosD += 1
        if nota[1] > maiornotaD:
            maiornotaD = nota[1]
    if nota[1] > maiornotageral:
        maiornotageral = nota[1]
        nomemaiornota = nota[0]
        turmamaiornota = nota[2]

print(f"{nomemaiornota} da turma {turmamaiornota} teve a maior nota, nota: {maiornotageral}")

print(f"A turma A teve {aprovadosA} aprovados")
print(f"A turma B teve {aprovadosB} aprovados")
print(f"A turma C teve {aprovadosC} aprovados")
print(f"A turma D teve {aprovadosD} aprovados")

print(f"A maior nota da turma A foi {maiornotaA}")
print(f"A maior nota da turma B foi {maiornotaB}")
print(f"A maior nota da turma C foi {maiornotaC}")
print(f"A maior nota da turma D foi {maiornotaD}")
