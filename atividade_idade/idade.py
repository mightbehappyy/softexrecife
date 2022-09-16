correto = False
while correto != True:
    try:
        nome = input("Digite um nome: ")
        idade = int(input("Digite um ano de nascimento entre 1922 e 2021: "))
        print(f"Nome do usuário: {nome}")
        print(f"Idade do usuário: {2022 - idade}")
        correto = True
    except:
        print("Digite um valor ou nome válido.")
        correto = False
