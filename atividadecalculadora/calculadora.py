num1 = int(input("Digite um valor: "))
num2 = int(input("Digite outro valor: "))
print("Digite a operção que deseja: \n 1. Soma \n 2. Subtração \n 3. Multiplicação \n 4. Divisão")
operacao = int(input("Operação: "))

def calculadora(num1, num2, operacao):
    if operacao == 1:
        print(num1 + num2)
    elif operacao == 2:
        print(num1 - num2)
    elif operacao == 3:
        print(num1 * num2)
    elif operacao == 4:
        print(num1 / num2)
    else:
        print(0)

calculadora(num1, num2, operacao)
