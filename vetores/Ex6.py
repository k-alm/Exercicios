lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista_invertida = []

for i in range(len(lista)-1, -1, -1):
    lista_invertida.append(lista[i])

print(lista_invertida)
