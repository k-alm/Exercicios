valor = int(input("Digite um valor: "))

print("TABUADA DO ", valor)

[print(f"{valor} * {i} = {valor * i}") for i in range(1, 11)]