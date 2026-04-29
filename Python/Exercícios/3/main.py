from utils import somar, media, eh_par, criar_usuario

a = 10
b = 20
print(somar(a, b))

lista = [10,25,40,55]
print(media(lista))

numero = int(input("Digite um número para verificar se é par: "))
sim = (eh_par(numero))
if sim:
    print(f"O número {numero} é par!")
else:
    print(f"O número {numero} é ímpar!")

nome = input("Digite o nome: ")
idade = int(input("Digite a idade: "))
usuario = criar_usuario(nome, idade)
print(f"Usuario criado: {usuario}")