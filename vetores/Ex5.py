lista = []
soma = 0

for i in range(20):
    valor = int(input("Digite um número: "))
    lista.append(valor)

    if i < 10:
        soma += valor

print("Soma dos 10 primeiros elementos do vetor: ", soma)




