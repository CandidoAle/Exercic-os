"""Exercício 24

- Ler número inteiro
- Devolver a soma de seus divisores (exceto ele mesmo)
"""

num = int(input('Inserir o número: '))
num_v = num
divisores = []

while num_v != 0:
    if num % num_v == 0:
        divisores.append(num_v)
    num_v -= 1

divisores_ord = sorted(divisores)
divisores_ord.pop()

soma_divisores = sum(divisores_ord)

print(f'A soma é: {soma_divisores}')