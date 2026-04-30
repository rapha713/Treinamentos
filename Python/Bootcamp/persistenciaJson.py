import json
import os
from utils import criar_usuario

ARQUIVO = "bootcamp.json" #GPToca

if os.path.exists(ARQUIVO):
    with open(ARQUIVO, "r") as f:
        try:
            bootcamp = json.load(f)
        except:
            bootcamp = []
else:
    bootcamp = []
    
nome = input("Digite o nome de usuário: ")
idade = input("Digite a idade do usuário: ")

user = criar_usuario(nome, idade)
bootcamp.append(user)

with open("bootcamp.json", "w") as f:
    json.dump(bootcamp, f, indent=4)

print(bootcamp)