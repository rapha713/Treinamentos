#Funções ficam na pasta utils

def saudacao():
    print("Olá!")
    
saudacao()

def saudacao1(nome):
    print(f"Olá, {nome}")

saudacao1("Raphael")

def somar(a, b):
    return a + b

resultado = somar(10, 5)
print(resultado)

def saudacao2(nome="Visitante"):
    print(f"Olá, {nome}")

saudacao2()

def criarUsuario(nome, idade):
    return {"nome": nome, "idade": idade}

criarUsuario("Raphael", "13")

#Funções lambda

dobro = lambda x:x*2

print(dobro(5))

numeros = [1, 2, 3, 4]

dobrados = list(map(lambda x: x * 2, numeros))
print(dobrados)

vendas = [
    {"produto": "A", "valor": 100},
    {"produto": "B", "valor": 300}
]

ordenado = sorted(vendas, key=lambda x: x["valor"])
print(ordenado)