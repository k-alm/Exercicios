meses = int(input("Você está na empresa há quantos meses?\n"))
vendas = int(input("Qual o valor total de suas vendas?\n"))

anos = meses / 12

if (meses < 6) or (anos < 2 and vendas < 5000) or (anos < 5 and vendas < 25000):
    print("O funcionário está demitido.")
else:
    print("O funcionário não está demitido.")


