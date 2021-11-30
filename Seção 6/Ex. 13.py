"""Exercício 13

- Receber um número N positivo e par
- Imprimir os números pares de zero até N
"""

N = int(input('Inserir Número: '))
cont = 0

while N % 2 or N < 0:
    print('O Número deve ser par e positivo.')
    N = int(input('Inserir Número: '))

while cont < N + 1:
    if cont % 2 == 0:
        print(cont)
    cont += 1
