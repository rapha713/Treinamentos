#sistema cadastro
def cadastrar_usuario(lista):
    user = input("Nome: ")
    age = int(input("Idade: "))
    #correção GPToca append altera lista e não usar return
    lista.append({"nome": user, "idade": age})

def lista_usuarios(lista):
    for u in lista:
        #correção GPToca não colocar return dentro de loop
        print("Nome:",u["nome"], "-", "Idade:", u["idade"])

def menu():
    print("\n1 - Cadastrar")
    print("2 - Listar")
    print("3 - Sair")
    #correção GPToca colocar input para lista
    return input("Escolha: ")