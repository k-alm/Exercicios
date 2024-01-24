qntd = 0

while qntd <= 50:
    qntd = int(input("Quantidade de produtos: "))

    print("-=" * 20, " TABELA DE PREÇOS ", "-=" * 20)

    for i in range(1, qntd + 1):
        print(f"Item {i} | Valor da conta: {i * 1.99:.2f}")

    print("-=" * 40)