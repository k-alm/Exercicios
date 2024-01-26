clientes = []

def cadastrar_cliente():
    codigo = int(input("Digite o código [0 = Encerrar Cadastro]: "))

    if codigo == 0: return None

    altura = int(input("Digite a altura em cm: "))
    peso = int(input("Digite o peso em kg: "))

    cliente = {"codigo": codigo, "altura": altura, "peso": peso}
    return cliente


def calcular_media(lista):
    return sum(lista) / len(lista)


while True:
    cliente = cadastrar_cliente()

    if cliente == None: break

    clientes.append(cliente)

alturas = [cliente["altura"] for cliente in clientes]
pesos = [cliente["peso"] for cliente in clientes]

mais_alto = max(clientes, key=lambda x: x["altura"])
mais_baixo = min(clientes, key=lambda x: x["altura"])
menos_magro = max(clientes, key=lambda x: x["peso"])
mais_magro = min(clientes, key=lambda x: x["peso"])

media_altura = calcular_media(alturas)
media_peso = calcular_media(pesos)

print(f"Média das alturas: {media_altura} | Média dos pesos: {media_peso}\n")

print(f"Cliente mais alto: {mais_alto} | Cliente mais baixo: {mais_baixo}\nCliente mais magro: {mais_magro} | Cliente menos magro: {menos_magro}")