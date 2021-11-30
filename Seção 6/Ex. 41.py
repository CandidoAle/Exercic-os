"""Exercício 41

- Calcular Req de dois resistores associados em paralelo.
- Calcular até que o usuário digite 0
"""

while True:
    R1 = float(input('Entrar com Resistor 1: '))
    if R1 == 0:
        break
    R2 = float(input('Entrar com Resistor 2: '))
    if R2 == 0:
        break
    Req = (R1 * R2) / (R1 + R2)
    print(f'A Req = {Req} para os Resistores {R1} e {R2} associados em paralelo')

