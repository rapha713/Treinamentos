from utils import calcular_total, calcular_media, maior_venda, menor_venda, vendas_acima_media
#Lista com variaveis
vendas = [
    {"produto": "A", "valor": 100},
    {"produto": "B", "valor": 250},
    {"produto": "C", "valor": 400},
    {"produto": "D", "valor": 150},
    {"produto": "E", "valor": 300}
]

#correção GPToca
valores = [item["valor"] for item in vendas]

print("Lista de dicionários\n")

soma = calcular_total(valores)
print("Total vendido: ", soma)

media = calcular_media(valores)
print("Média por vendas: ", media)

maior = maior_venda(valores)
print("Maior venda: ", maior)

menor = menor_venda(valores)
print("Menor venda: ", menor)

venda_acima = vendas_acima_media(valores)
print("Venda acima da média: ", venda_acima)

#Lista sem variaveis
print("\nLista comum\n")

vendas = [100, 250, 400, 150, 300]

soma = calcular_total(vendas)
print("Total vendido: ", soma)

media = calcular_media(vendas)
print("Média por vendas: ", media)

maior = maior_venda(vendas)
print("Maior venda: ", maior)

menor = menor_venda(vendas)
print("Menor venda: ", menor)

venda_acima = vendas_acima_media(vendas)
print("Venda acima da média: ", venda_acima)