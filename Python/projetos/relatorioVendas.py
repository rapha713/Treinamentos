vendas = [
    {"produto": "A", "valor": 100},
    {"produto": "B", "valor": 250},
    {"produto": "C", "valor": 400},
    {"produto": "D", "valor": 150},
    {"produto": "E", "valor": 300}
]

soma = sum(item["valor"] for item in vendas)
qtd = len(vendas)
media = soma / qtd
maior = max(item["valor"] for item in vendas)
menor = min(item["valor"] for item in vendas)

print("Total vendido: ", soma)
print("Média por vendas: ", media)
print("Maior venda: ", maior)
print("Menor venda: ", menor)

acima_media = [v for v in vendas if v["valor"] > media]

for v in acima_media:
    print("Venda acima da média:", v)