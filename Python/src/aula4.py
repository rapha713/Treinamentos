import json
import os

#ARQUIVOS
#"w" - sobrescreve
#"a" - adiciona
#"r" - lê

with open("arquivo.txt", "w") as f:
    f.write("Olá mundo")
    
with open("arquivo.txt", "r") as f:
    conteudo = f.read()
    print(conteudo)
    
    
#--------------------------------------------------------------------------------#

#JSON
dados = [{"nome": "Raphael", "idade": 30}]

with open("usuarios.json", "w") as f:
    json.dump(dados,f)
    
with open("usuarios.json", "r") as f:
    dados = json.load(f)
    
print(dados)

#para erro 'FileNotFoundError'
if os.path.exists("usuarios.json"):
    with open("usuarios.json", "r") as f:
        usuarios = json.load(f)
else:
    usuarios = []
