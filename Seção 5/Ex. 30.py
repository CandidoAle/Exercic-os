"""Exercício 30

Fazer programa que receba 3 números e mostre-os em ordem crescente
"""

num1 = float(input('Inserir número 1: '))
num2 = float(input('Inserir número 2: '))
num3 = float(input('Inserir número 3: '))

numeros = [num1, num2, num3]
numeros.sort()

print(f'Os números em ordem crescente: {numeros[0]}, {numeros[1]}, {numeros[2]}.')