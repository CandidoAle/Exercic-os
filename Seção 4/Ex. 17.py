"""Exercício 17 (40)

Calcular valor a ser pago para o encanador que trabalha por 30/dia - 8% de IR
"""

dias = int(input('Número de dias da prestação de serviço: '))

IR = 0.08

valor = dias * 30.0 * (1 - IR)
print(f'Valor a ser pago para o prestador é {valor}')


