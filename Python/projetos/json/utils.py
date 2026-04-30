from database import salvar_dados

def cadastrar_usuario(lista):
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    
    #PARA VERIFICAR SE JÁ EXISTE O NOME DO USUARIO
    # if any(u["nome"] == nome for u in lista):
    #     print("Usuário já existe!")
    # else:
    lista.append({"nome": nome, "idade": idade})
    salvar_dados(lista)

    print("Usuário cadastrado com sucesso!")

def listar_usuarios(lista):
    if not lista:
        print("Nenhum usuário cadastrado.")
        return

    for i, u in enumerate(lista):
        print(f"{i} - Nome: {u['nome']} | Idade: {u['idade']}")

def atualizar_usuario(lista):
    listar_usuarios(lista)

    try:
        id = int(input("Digite o id do usuário para atualizar: "))
    except:
        print("Entrada inválida")
        return

    if id < 0 or id >= len(lista):
        print("Id inválido")
        return

    nome = input("Novo nome: ")
    idade = int(input("Nova idade: "))

    lista[id]["nome"] = nome
    lista[id]["idade"] = idade

    salvar_dados(lista)

    print("Usuário atualizado com sucesso!")

def remover_usuario(lista):
    listar_usuarios(lista)

    try:
        id = int(input("Digite o id do usuário para remover: "))
    except:
        print("Entrada inválida")
        return

    if id < 0 or id >= len(lista):
        print("Id inválido")
        return

    removido = lista.pop(id)

    salvar_dados(lista)

    print(f"Usuário {removido['nome']} removido com sucesso!")

def menu():
    print("\n1 - Cadastrar")
    print("2 - Listar")
    print("3 - Atualizar")
    print("4 - Remover")
    print("0 - Sair")
    return input("Escolha: ")