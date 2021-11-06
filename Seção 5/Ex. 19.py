"""Exercício 19

Entrada - Numero

Devolver se é divisível por 3 ou por 5
Devolver quando é disível simutaneamente pelos 2
"""

num = int(input('Inserir número: '))

if num % 3 == 0 and num % 5 == 0:
    print(f'{num} é divisível por 3 e 5.')
elif num % 3 == 0:
    print(f'{num} é divisível por 3.')
elif num % 5 == 0:
    print(f'{num} é divisível por 5.')
else:
    print(f'{num} não é divisível nem por 3 nem por 5.')