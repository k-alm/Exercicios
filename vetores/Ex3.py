lista = []

for i in range(10):
    numero = int(input("Digite um número: "))
    lista.append(numero)

pares = [item for item in lista if item % 2 == 0]
print(pares)