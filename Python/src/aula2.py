#for
for i in range(5):
    print(i)

#range (inicio, fim, passo)
for r in range(1, 10, 2):
    print(r)
    
nomes = ["Ana", "João", "Carlos"]
for nome in nomes:
    print(nome)
    
for i,nome in enumerate(nomes):
    print(i, nome)
    
########################################################################################

#while
contador = 0
while contador < 5:
    print(contador)
    contador += 1

########################################################################################
    
#break
for i in range(10):
    if i == 5:
        break
    print(i)

for i in range(10):
    if i % 2 == 0:
        continue
    print(i)
    
########################################################################################

numeros = [0,1,2,3,4,5]
print(numeros[1:4])
print(numeros[:3])
print(numeros[::2])

print(numeros[::-1])

########################################################################################

numeros = [5,2,9,1]
numeros.sort()
print(numeros)

numeros.reverse()
print(numeros)

########################################################################################

numeros=[1,2,3,4]
dobro = [n * 2 for n in numeros]
pares = [n for n in numeros if n % 2 == 0]
print(dobro)
print(pares)

nomes = ["ana", "joao", "carlos"]
maiusculos = [nome.upper() for nome in nomes]
print(maiusculos)