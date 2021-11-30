"""Exercício 14

- Receber um número par positivo
- Imprimir pares de N até zero

"""

N = int(input('Inserir número: '))

while N % 2 != 0 or N < 0:
    print('O número deve ser positivo e par.')
    N = int(input('Inserir número: '))

while N >= 0:
    if N % 2 == 0:
        print(N)
    N -= 1