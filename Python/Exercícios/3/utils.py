def somar(a, b):
    return (a + b)

def media(lista):
    return sum(lista) / len(lista) if lista else 0
    
def eh_par(numero):
    return numero % 2 == 0

def criar_usuario(nome, idade):
    return {"nome": nome, "idade": idade}