n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

def validacao(n1, n2):
    if(n2 > n1):
        return True
    else:
        return False


print(validacao(n1, n2))