"""Exercício 54

- Receber um número e dizer se ele é primo ou não.

"""

n = int(input('Inserir número: '))
contador = n - 1

while True:

    if contador == 1:
        print('Número é primo')
        break
    elif n % contador == 0:
        print('Número não é primo')
        break

    contador -= 1

