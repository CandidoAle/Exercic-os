"""Exercício 8

Ler 2 numeros interos
Verificar o maior deles - imprimir
Imprimir diferença entre ambos
"""

num1 = int(input('Inserir primeiro número: '))
num2 = int(input('Inserir segundo número: '))

if num1 > num2:
    print(f'{num1} é maior que {num2}.')
    print(f'E a diferença entre eles é {num1 - num2}')
elif num1 < num2:
    print(f'{num2} é maior que {num1}.')
    print(f'E a diferença entre eles é {num2 - num1}')
else:
    print(f'Os números são iguais.')
    print(f'E a diferença entre eles é 0')
