nome = str(input("Digite seu nome: "))
idade = int(input("Digite sua idade: "))
salario = int(input("Digite seu salário: "))
sexo = str(input("Digite seu sexo [M/F]: ").lower()[0])
estado_civil = str(input("Digite seu estado civil [S/C/V/D]: ").lower()[0])

def validacao(nome, idade, salario, sexo, estado_civil):
    if len(nome) > 3 and (idade >= 0 and idade <= 150) and salario > 0:
        if sexo == "f" or sexo == "m":
            if estado_civil in ("s", "c", "v", "d"):
                return True
    else:
        return False
    

print(validacao(nome, idade, salario, sexo, estado_civil))
