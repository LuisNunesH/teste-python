import pandas as pd

# Leitura do csv
df = pd.read_csv('../csv/vendas_produtos.csv')

# Cálculo do faturamento total por produto
df['faturamento'] = df['quantidade'] * df['preco_unitario']
faturamento_por_produto = df.groupby('produto')['faturamento'].sum()

# Produto com maior e menor faturamento
maior_faturamento = faturamento_por_produto.idxmax()
menor_faturamento = faturamento_por_produto.idxmin()

# Resultados
print("Faturamento total por produto:")
print(faturamento_por_produto.to_string())

print(f"\nProduto com maior faturamento: {maior_faturamento}")
print(f"Produto com menor faturamento: {menor_faturamento}")