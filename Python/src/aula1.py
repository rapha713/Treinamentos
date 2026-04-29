'int idade = 29;'
idade = 29

'string nome = "Raphael";'
nome = "Raphael"

'Console.WriteLine("Olá, " + nome + "! Você tem " + idade + " anos.");'
print("Olá, " + nome + "! Você tem " + str(idade) + " anos.")

########################################################################################

'if (idade >= 18) { Console.WriteLine("Maior"); }'
if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")
    
########################################################################################

a = 10
b = 5

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)


########################################################################################
numeros = [1, 2, 3, 4]
numeros.append(5)
print(numeros)
print(numeros[0])

for n in numeros:
    print(n)
    
########################################################################################

usuario = {
    "nome": "Raphael",
    "idade": 29
}
print(usuario["nome"])
usuario["email"] = "teste@email.com"