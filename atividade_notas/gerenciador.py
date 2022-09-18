import pandas as pd

df = pd.read_csv("atividade_notas/dataframe_notas.csv") # Lê o arquivo

maior_falta = df["Faltas"].max() # maior número de faltas
media_geral = (df['Nota 1'].median() + df["Nota 2"].median())/ 2 # media geral
df['Media_individual'] = (df["Nota 1"] + df["Nota 2"]) / 2 # Cria uma nova coluna e insere a média individual das duas notas do aluno

maior_media_invidividual = df["Media_individual"].max() # Encontra a maior media da coluna criada

df["Situacao"] = 'Reprovado' # Define uma coluna situação em que todos os alunos estão reprovados

df.loc[(df["Media_individual"] >= 7) & (df["Faltas"] < 6), "Situacao"] = "Aprovado" # Condicional em que caso a média individual do aluno for maior que 7
                                                                                    # e que este aluno não tenha mais que 5 faltas a situacao será de aprovado
df.to_csv('notas_alunos.csv', index= False) # Cria um novo arquivo csv

print(f"O maior número de faltas foi {maior_falta} faltas")                        
print(f"A média geral da turma foi {media_geral}")
print(f"A maior média individual foi {maior_media_invidividual}")
