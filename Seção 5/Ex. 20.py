"""Exercício 20

A B C podem ser lado de um triângulo?
Se sim - qual tipo de triangulo?
"""

A = float(input('Inserir comprimento do lado A do triângulo: '))
B = float(input('Inserir comprimento do lado B do triângulo: '))
C = float(input('Inserir comprimento do lado C do triângulo: '))

if A < (B+C) and B < (A+C) and C < (A+B):
    if A == B and B == C:
        print(f'O triangulo ABC é equilátero.')
    elif A == B or B == C or A == C:
        print(f'O triângulo ABC é isosceles.')
    else:
        print(f'O triângulo ABC é escaleno.')
else:
    print(f'Valores invalidos pois ABC não é triangulo.')