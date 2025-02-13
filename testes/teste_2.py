import pandas as pd

df = pd.read_csv('../csv/vendas_produtos.csv')

df['faturamento'] = df['quantidade'] * df['preco_unitario']
faturamento_por_produto = df.groupby('produto')['faturamento'].sum()

maior_faturamento = faturamento_por_produto.idxmax()
menor_faturamento = faturamento_por_produto.idxmin()

print("Faturamento total por produto:")
print(faturamento_por_produto.to_string())

print(f"\nProduto com maior faturamento: {maior_faturamento}")
print(f"Produto com menor faturamento: {menor_faturamento}")