"""Exercício 39

- Calcular área de um triangulo
- Inputs: Base e altura

"""

base = float(input('Fornecer comprimento da base do triangulo: '))

while base <= 0:
    print('A base deve ser postiva')
    base = float(input('Fornecer comrpimento da base: '))

altura = float(input('Fornecer altura do triangulo: '))

while altura <= 0:
    print('A altura deve ser positiva')
    altura = float(input('Fornecer altura do triangulo: '))

area = base * altura * 0.5

print(f'A área do triangulo é {area}')