"""
Exercício 4 (7)
Mostrar qual número é maior ou se são iguais
"""

num1 = float(input('Escolher primeiro número: '))
num2 = float(input('Escolher segundo número: '))

if num1 == num2:
    print('Os números são iguais.')
elif num1 > num2:
    print(f'{num1} é o maior')
else:
    print(f'{num2} é o maior')
