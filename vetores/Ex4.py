lista = []

for i in range(10):
    numero = int(input("Digite um número: "))
    lista.append(numero)

maiores_que_dez = [item for item in lista if item > 10]

print(maiores_que_dez)
