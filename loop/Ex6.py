def resumo(lista_produtos, total, troco):
    contador = 0

    for i in lista_produtos:
        contador += 1
        print(f"Produto {contador}: R$ {i:.2f}")

    print(f"""Total: R$ {total:.2f}\nTroco: R$ {troco:.2f}""")


while True:
    produtos = []
    valor = None

    while valor != 0:
        valor = float(input("Digite o valor do produto: "))
        produtos.append(valor)

    total = sum(produtos)

    print(f"Total da compra: {total}")

    pagamento = float(input("Qual o valor do pagamento, em dinheiro? "))
    troco = pagamento - sum(produtos)

    print(f"Troco: {troco:.2f}")

    print("Lojas Tabajara")
    resumo(produtos, total, troco)




