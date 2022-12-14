usuario = input("Digite alguma frase ou nome. ")

caps = usuario.upper()
capitalizar = usuario.capitalize()
codificar = usuario.encode()
contar = usuario.count("a")

print(f"A string codificada é: {codificar}")
print(f"A string em capslock é: {caps}")
print(f"A string captalizada é: {capitalizar}")
print(f"A contade da letra A para a string é {contar}")


