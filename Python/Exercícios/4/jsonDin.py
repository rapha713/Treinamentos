from utils import criar_usuario
import json
import os

nome = input("Digite o nome: ")
idade = input("Digite a idade: ")
user = [criar_usuario(nome, idade)]

with open("dinamico.json", "w") as f:
    json.dump(user, f)
    
if os.path.exists("dinamico.json"):
    with open("dinamico.json", "r") as f:
        arquivo = json.load(f)
else:
    arquivo = []
    
print(arquivo)