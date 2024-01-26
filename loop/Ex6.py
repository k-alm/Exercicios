def resumo(lista_valores, total, troco):
    for i, valor in enumerate(lista_valores, start=1):
        print(f"Produto {i}: R$ {valor:.2f}")

    print(f"Total: R$ {total:.2f}\nTroco: R$ {troco:.2f}")


while True:
    valores = []
    valor = None

    while valor != 0:
        valor = float(input("Digite o valor do produto: "))
        valores.append(valor)

    total = sum(valores)

    print(f"Total da compra: {total}")

    pagamento = float(input("Qual o valor do pagamento, em dinheiro? "))
    troco = pagamento - sum(valores)

    print(f"Troco: {troco:.2f}")

    print("Lojas Tabajara")
    resumo(valores, total, troco)




