"""Exercício 40

- Ler valor do produto
- Devolver valor final calculando % dist e % imposto
"""

valor_produto = float(input('Inserir valor do produto: '))

if valor_produto <= 12000:
    valor_final = valor_produto * 1.05
elif 12000 < valor_produto <= 25000:
    valor_final = valor_produto * 1.25
elif valor_produto > 25000:
    valor_final = valor_produto * 1.35

print(f'Valor final para o consumidor {valor_final}')

