import json

with open("dados.json", "r") as f:
    dados = json.load(f)
    
for u in dados:
    print(f"Nome: {u['nome']} - Idade: {u['idade']}")
    
#PARA LER ARQUIVOS DINAMICAMENTE
# arquivo = input("Digite o nome do arquivo: ")
# with open(arquivo, "r") as f:
#     dados = json.load(f)
# print(dados)