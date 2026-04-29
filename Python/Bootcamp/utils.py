#sistema de vendas
def calcular_total(vendas):
    return sum(vendas)

def calcular_media(vendas):
    return sum(vendas) / len(vendas) if vendas else 0

def maior_venda(vendas):
    return max(vendas)

def menor_venda(vendas):
    return min(vendas)

#correção GPToca
def vendas_acima_media(vendas):
    media = (sum(vendas) / len(vendas) if vendas else 0)
    return [v for v in vendas if v > media]