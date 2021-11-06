"""Exercício 24

MG - 7%
SP - 12%
RJ - 15%
MS - 8%

Entrada = Valor e destino.
Saída = Valor final (valor+impostos) ou estado invalido
"""

valor = float(input('Inserir valor do produto: '))
estado = input('Estado destino: ')

estados = {'MG': 0.07, 'SP': 0.12, 'RJ': 0.15, 'MS': 0.08}

if estado != 'MG' and estado != 'SP' and estado != 'RJ' and estado != 'MS':
    print(f'Não fazemos entregas para este estado: {estado}')
else:
    valor_final = estados[estado] * valor + valor
    print(f'O total do pedido + impostos é {valor_final}')
