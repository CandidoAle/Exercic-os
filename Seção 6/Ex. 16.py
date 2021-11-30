"""Exercício 16

- Ler número inteiro positivo impar
- Imprimir numeros de N até 1 (somente os impares)
"""

N = int(input('Inserir número: '))

while N < 0 or N % 2 == 0:
    print('O número deve ser impar e positivo.')
    N = int(input('Inserir número: '))

while N >= 0:
    if N % 2 != 0:
        print(N)
    N -=1

