"""Exercício 33

- Cálculo de Ajuste e Classificação -
    * Ler preço antigo ok
    * Devolver % de reajuste ok
    * Devolver preço novo calculado ok
    * Devolver Classificação

"""
# Calculo do preço novo

preco_antigo = float(input('Preço do produto: '))

if preco_antigo <= 50:
    preco_novo = preco_antigo * 1.05
elif preco_antigo > 50 and preco_antigo <= 100:
    preco_novo = preco_antigo * 1.10
elif preco_antigo > 100:
    preco_novo = preco_antigo * 1.15

porcentagem = (preco_novo/preco_antigo - 1) * 100

print('O produto recebeu %.1f por cento de ajuste.' %porcentagem)
print(f'O novo preço do produto é R$ %.2f' %preco_novo)

# Classificação do preço novo

if preco_novo <= 80:
    print('Novo preço é classificado como Barato.')
elif preco_novo > 80 and preco_novo <=120:
    print('Novo preço é classificado como Normal.')
elif preco_novo > 120 and preco_novo <= 200:
    print('Novo preço é classificado como Caro.')
elif preco_novo > 200:
    print('Novo preço é classificado como Muito Caro.')

