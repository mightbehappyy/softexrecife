from random import randint
lista = [randint(0,20),randint(0,20),randint(0,20),randint(0,20),randint(0,20),]
print("="*10)
print("Lista desorganizada")
print(lista)
print("="*10)
for n in lista:
    a = 0
    b = 0
    for v,c in enumerate (lista):
        a = lista[v]
        if v < len(lista)-1:
            b = lista[v+1]
        else:
            break
        if a > b:
            lista[v], lista[v+1] = lista[v+1], lista[v]
        else:
            continue
print("Lista organizada")
print(lista)