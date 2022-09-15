from random import randint
nome_aluno = "Pedro Luiz Rodrigues de Assis"
nota1 = randint(0,10)
nota2 = randint(0,10)
faltas = randint(0,6)
media = (nota1 + nota2)/ 2

print(f"Nome do aluno: {nome_aluno}")
print(f"Média: {media}")
print(f"Faltas: {faltas}")
if media > 7.0 and faltas <= 3:
    print("APROVADO")
else:
    print("REPROVADO")

