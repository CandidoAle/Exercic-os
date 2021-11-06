"""
Exercício 2
Calcular raiz quadrada de um número real
"""

num = float(input('Inserir número: '))

if num > 0:
    res = num ** 0.5
    print(f'O resultado é {res}')
else:
    print(f'O número {num} é invalido')
