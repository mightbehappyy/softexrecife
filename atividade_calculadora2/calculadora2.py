print("Digite a operção que deseja: \n 0. Sair\n 1. Soma \n 2. Subtração \n 3. Multiplicação \n 4. Divisão")
operacao = int(input("Escolha uma operação: "))

while operacao != 0:
    num1 = int(input("Digite um valor: "))
    num2 = int(input("Digite outro valor: "))
    def calculadora(num1, num2, operacao):
        if operacao == 1:
            print(f"Resultado: {num1 + num2}")
        elif operacao == 2:
            print(f"Resultado: {num1 - num2} ")
        elif operacao == 3:
            print(f"Resultado: {num1 * num2}")
        elif operacao == 4:
            print(f"Resultado: {num1 / num2}")
        else:
            print(0)
    calculadora(num1, num2, operacao)
    print("\nDigite a operção que deseja: \n 0. Sair\n 1. Soma \n 2. Subtração \n 3. Multiplicação \n 4. Divisão")
    operacao = int(input("Escolha uma operação: "))
