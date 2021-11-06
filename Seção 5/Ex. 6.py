"""Exercicio 6 (4)

Receber um numero

Se positivo
    Devolver o quadrado
    Devolver a raiz
"""
import math

numero = float(input('Insira um número: '))

if numero > 0:
    print(f'O quadrado de {numero} é {numero ** 2}')
    print(f'A raiz quadrada de {numero} é {math.sqrt(numero)}')
