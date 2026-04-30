import json
import os

dados = [{"nome": "Raphael Oliveira", "idade": 30}]

with open("dados.json", "w") as f:
    json.dump(dados,f)
    
if os.path.exists("user.json"):
    with open("user.json", "r") as f:
        usuarios = json.load(f)
elif os.path.exists("dados.json"):
    with open("dados.json", "r") as f:
        usuarios = json.load(f)
else:
    usuarios = []
    
print(usuarios)