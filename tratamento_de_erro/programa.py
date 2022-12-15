try:
    idade = int(input("Digite sua idade em valor numerico "))
    print(f"Você tem {idade}")
except ValueError as error:
    print("ERRO \Você não digitou um valor numerico!!")
