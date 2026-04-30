import json
import os

ARQUIVO = "usuarios.json"

def carregar_dados():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r") as f:
            try:
                return json.load(f)
            except:
                return []
    return []

def salvar_dados(dados):
    with open(ARQUIVO, "w") as f:
        json.dump(dados, f, indent=4)