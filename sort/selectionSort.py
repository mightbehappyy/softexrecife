import random 
lista = []
n = 30
for i in range(n):
    lista.append(random.randrange(1, 30, 2))


def selectionSort(lista, tamanho):
    for step in range(tamanho):
        menor_numero = step

        for i  in range(step + 1, tamanho):
            if lista[i] < lista[menor_numero]:
                menor_numero = i
    
        lista[step], lista[menor_numero] = lista[menor_numero], lista[step]


tamanho = len(lista)
selectionSort(lista, tamanho)
print(lista)
