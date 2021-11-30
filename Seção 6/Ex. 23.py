"""Exercício 23

- Ler numero inteiro positivo
- Imprimir seus divisores
"""

num = int(input('Inserir o número: '))
num_v = num
divisores = []

while num_v != 0:
    if num % num_v == 0:
        divisores.append(num_v)
    num_v -= 1

print(f'D({num}) = {sorted(divisores)}')
