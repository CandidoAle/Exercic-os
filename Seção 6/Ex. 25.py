"""Exercício 25

- Programa que some todos os números naturais abaixo de 1000 que são multiplos
de 3 ou 5.

"""

num = 1000
mult_3_5 = []

while num != 0:
    if num % 3 == 0 or num % 5 == 0:
        mult_3_5.append(num)
    num -= 1

print(f'Lista de multiplos de 3 e 5: {mult_3_5}')

soma = sum(mult_3_5)

print(f'A soma deles é {soma}')