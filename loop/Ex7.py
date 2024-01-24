clientes = []
codigo = None

altura_max = 0
peso_max = 0

altura_min = 999
peso_min = 999

while True:
    codigo = int(input("Digite o código [0 = Encerrar Cadastro]: "))
    if codigo == 0: break

    altura = int(input("Digite a altura em cm: "))
    peso = int(input("Digite o peso em kg: "))

    cliente = {"codigo": codigo, "altura": altura, "peso": peso}
    clientes.append(cliente)

for i in clientes:
    if i["altura"] > altura_max:
        altura_max = i["altura"]
    elif i["altura"] < altura_min:
        altura_min = i["altura"]

    if i["peso"] > peso_max:
        peso_max = i["peso"]
    elif i["peso"] < peso_min:
        peso_min = i["peso"]

for i in clientes:
    if altura_max == i["altura"]:
        print(f"Cliente mais alto:\nCódigo: {i["codigo"]}, Altura: {i["altura"]}, Peso: {i["peso"]}")
    elif altura_min == i["altura"]:
        print(f"Cliente mais baixo:\nCódigo: {i["codigo"]}, Altura: {i["altura"]}, Peso: {i["peso"]}")

    if peso_max == i["peso"]:
        print(f"Cliente menos magro:\nCódigo: {i["codigo"]}, Altura: {i["altura"]}, Peso: {i["peso"]}")
    elif peso_min == i["peso"]:
        print(f"Cliente mais magro:\nCódigo: {i["codigo"]}, Altura: {i["altura"]}, Peso: {i["peso"]}")

print(f"Média das alturas: {sum(clientes["altura"])/len(clientes)} | Média dos pesos: {sum(clientes["peso"])/len(clientes)} ")
# print(f"Maior altura: {altura_max} | Menor altura: {altura_min}\nMaior peso: {peso_max} | Menor peso: {peso_min}")
