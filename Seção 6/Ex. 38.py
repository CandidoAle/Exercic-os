"""Exercício 40

- Faça um programa que leia vários número positivos. Parar quando for fornecido um negativo
- Devolver maior e maior número fornecido
"""

num = int(input('Fornecer número: '))
numeros = []

while not num < 0:
    numeros.append(num)
    num = int(input('Fornecer número: '))

max = max(numeros)
min = min(numeros)

print(f'O maior número fornecido é {max}')
print(f'O menor número forcedido é {min}')