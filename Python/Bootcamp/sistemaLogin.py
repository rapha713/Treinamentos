user_correto = "admin"
senha_correta = "1234"

usuario = input("Digite o usuário: ")
senha = input("Digite a senha: ")

for i in range(3):
     if usuario == user_correto and senha == senha_correta:
        print("Login bem-sucedido!")
        break
     else:
        print("Usuário ou senha incorretos. Tente novamente.")
        print(f"Você tem {2 - i} tentativas restantes.")
        usuario = input("Digite o usuário: ")
        senha = input("Digite a senha: ")