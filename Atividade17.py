Leitor e Analisador de CSV

import csv

# Cria um arquivo de exemplo para o script funcionar
with open("vendas.csv", "w", newline="", encoding="utf-8") as f:
    f.write("produto,quantidade,preco\nTeclado,5,150.00\nMouse,10,80.00\nTeclado,2,150.00")

faturamento_produto = {}
faturamento_geral = 0.0

with open("vendas.csv", "r", encoding="utf-8") as f:
    leitor = csv.DictReader(f)
    for linha in leitor:
        prod = linha["produto"]
        total_linha = int(linha["quantidade"]) * float(linha["preco"])
        faturamento_produto[prod] = faturamento_produto.get(prod, 0) + total_linha
        faturamento_geral += total_linha

print("Por produto:", faturamento_produto)
print(f"Faturamento Geral: R$ {faturamento_geral:.2f}")
