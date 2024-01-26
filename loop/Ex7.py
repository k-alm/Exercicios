clientes = []

cliente_mais_alto = None
cliente_mais_baixo = None
cliente_mais_magro = None
cliente_menos_magro = None

soma_altura = 0
soma_peso = 0

while True:
    codigo = int(input("Digite o código [0 = Encerrar Cadastro]: "))

    if codigo == 0: break

    altura = int(input("Digite a altura em cm: "))
    peso = int(input("Digite o peso em kg: "))

    cliente = {"codigo": codigo, "altura": altura, "peso": peso}
    clientes.append(cliente)

for cliente in clientes:
    soma_altura += cliente["altura"]
    soma_peso += cliente["peso"]

    if cliente_mais_alto == None or cliente["altura"] > cliente_mais_alto["altura"]:
        cliente_mais_alto = cliente

    if cliente_mais_baixo == None or cliente["altura"] < cliente_mais_baixo["altura"]:
        cliente_mais_baixo = cliente

    if cliente_mais_magro == None or cliente["peso"] < cliente_mais_magro["peso"]:
        cliente_mais_magro = cliente

    if cliente_menos_magro == None or cliente["peso"] > cliente_menos_magro["peso"]:
        cliente_menos_magro = cliente

media_altura = soma_altura / len(clientes)
media_peso = soma_peso / len(clientes)

print(f"Média das alturas: {media_altura} | Média dos pesos: {media_peso}\n")

print(f"Cliente mais alto: {cliente_mais_alto} | Cliente mais baixo: {cliente_mais_baixo}\nCliente mais magro: {cliente_mais_magro} | Cliente menos magro: {cliente_menos_magro}")