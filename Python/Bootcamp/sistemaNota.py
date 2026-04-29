notas = []

while True:
    opcao = input("Digite a nota (para sair digite '-1'): ")
    if opcao == "-1":
        break
    
    notas.append(float(opcao))
    
media = sum(notas) / len(notas)
maior = max(notas)
menor = min(notas)

print("A média das notas: ", media)
print("A maior nota: ", maior)
print("A menor nota: ", menor)

for nota in notas:
    if nota > media:
        print("A nota", nota, "é maior que a média.")