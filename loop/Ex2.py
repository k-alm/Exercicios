user, senha = None, None

while True:
    user = str(input("Usuário: "))
    senha = str(input("Senha: "))

    if user == senha:
        print("O nome de usuário não pode ser igual à senha. Digite novamente.")
    else:
        break

print(f"User: {user} | Senha: {senha}")