"""Exercício 32

Ler código do produto e a quantidade.
Devolver produto e valor a ser pago.
"""

cardapio = {100: 'Cachorro Quente', 101: 'Bauru Simples', 102: 'Bauru com Ovo', 103: 'Hamburguer', 104: 'Cheeseburguer',
            105: 'Suco', 106: 'Refrigerante'}

preco = {100: 1.20, 101: 1.30, 102: 1.50, 103: 1.20, 104: 1.70, 105: 2.20, 106: 1.00}

codigo = int(input('Inserir código do produto: '))

while codigo != 100 and codigo != 101 and codigo != 102 and codigo != 103 and codigo != 104 and codigo != 105 and codigo != 106:
    print('Código do produto inválido.')
    print('Favor inserir um código existente.')
    codigo = int(input('Inserir código do produto: '))

qtd = int(input('Quantos itens?: '))

conta = preco[codigo] * qtd

print(f'Pedido: {qtd} {cardapio[codigo]}')
print(f'Total: {conta}')

