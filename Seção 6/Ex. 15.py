"""Exercício 15

- Ler número impar e positivo.
- Imprimir numero impares de 1 a N.
"""

N = int(input('Inserir número: '))
cont = 1

while N % 2 == 0 or N < 0:
    print('O número deve ser impar e positivo.')
    N = int(input('Inserir número: '))

while cont < N + 1:
    if cont % 2 != 0:
        print(cont)
    cont += 1