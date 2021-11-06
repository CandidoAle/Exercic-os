"""Exercício 25

Resolver equação de segundo grau.
"""

a = float(input('Inserir coeficiente a: '))
b = float(input('Inserir coeficiente b: '))
c = float(input('Inserir coeficiente c: '))

if a == 0:
    print('Não é uma equação de segundo grau: ')
else:
    delta = b ** 2 - (4 * a * c)
    if delta < 0:
        print('Não existe raiz real.')
    elif delta == 0:
        print('Existe uma raiz real.')
        x = (- b + delta ** 0.5)/(2 * a)
        print(f'A raiz é {x}.')
    else:
        print('Existem duas raizes real.')
        x1 = (- b + delta ** 0.5) / (2 * a)
        x2 = (- b - delta ** 0.5) / (2 * a)
        print(f'As raizes sãp {x1} e {x2}.')
