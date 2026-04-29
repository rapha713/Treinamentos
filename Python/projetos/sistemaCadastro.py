from utils import menu, cadastrar_usuario, lista_usuarios

usuario = []

# while True:
#     print("1 - Cadastrar")
#     print("2 - Listar")
#     print("3 - Sair")

#     opcao = input("Escolha: ")
#     if opcao == "1":
#         nome = input("Digite o nome: ")
#         idade = input("Digite a idade: ")
#         usuario.append({"nome": nome, "idade": idade})
#     elif opcao == "2":
#         for u in usuario:
#             print("Nome:",u["nome"], "-", "Idade:", u["idade"])
#     elif opcao == "3":
#         break
#     else:
#         print("Opção inválida. Tente novamente.")

while True:
    opcao = menu()
    
    if opcao == "1":
        cadastrar_usuario(usuario)
    elif opcao == "2":
        lista_usuarios(usuario)
    elif opcao == "3":
        print("Saindo...")
        break
    else:
        print("Opção inválida. Tente novamente!")