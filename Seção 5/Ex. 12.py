"""Exercício 12

Ler numero interiro

Se for negativo = Número invalido
Se for positivo = Calcular log
"""
import math

numero = int(input('Inserir número: '))

if numero < 0:
    print(f'Número {numero} é invalido.')
else:
    log = math.log10(numero)
    print(f'O log de {numero} é {log}')
