from utils import cadastrar_usuario, listar_usuarios, atualizar_usuario, remover_usuario, menu
from database import carregar_dados

usuarios = carregar_dados()

while True:
    opcao = menu()
    
    if opcao == "1":
        cadastrar_usuario(usuarios)
    elif opcao == "2":
        listar_usuarios(usuarios)
    elif opcao == "3":
        atualizar_usuario(usuarios)
    elif opcao == "4":
        remover_usuario(usuarios)
    elif opcao == "0":
        print("Saindo...")
        break
    else:
        print("Opção inválida!")