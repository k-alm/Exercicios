lista = []

for i in range(10):
    numero = int(input("Digite um número: "))
    lista.append(numero)

print("Números pares: ")
for i in lista:
    if i % 2 == 0:
        print(i)
