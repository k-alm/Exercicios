lista = []

for i in range(10):
    numero = int(input("Digite um número: "))
    lista.append(numero)

print("Números maiores ou iguais a 10: ")
for i in lista:
    if i >= 10:
        print(i)
