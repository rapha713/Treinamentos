numeros = []
    
while True:
    opcao = input("Digite um número (para sair digite '0'): ")
    if opcao == "0":
        break
    numeros.append(float(opcao))
        
    
qtd = len(numeros)
soma = sum(numeros)
media = soma / qtd if qtd > 0 else 0

print("Quantidade: ", qtd)
print("Soma: ",soma)
print("Média: ",media)