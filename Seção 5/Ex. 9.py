"""Exercício 9

Ler salário da PF
Ler valor da prestação do empréstimo

Caso prestação for maior que 20% do valor do salário -> Empréstimo não concedido
Se não -> Empréstimo concedido
"""

salario = float(input('Valor do salário do contratante: '))
prestacao = float(input('Valor da prestação do empréstimo: '))

limite = salario * 0.2

if prestacao > limite:
    print('Empréstimo não concedido.')
else:
    print('Empréstimo concedido.')
