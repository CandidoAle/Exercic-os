"""Exercício 7 (3)

Ler um número real

Se positivo
    Devolver raiz quadrada
Se não
    Devolver o quadrado
"""
import math

numero = float(input('Inserir número: '))

if numero >= 0:
    print(f'A raiz quadrada de {numero} é {math.sqrt(numero)}')
else:
    print(f'O quadrado de {numero} é {numero ** 2}')
