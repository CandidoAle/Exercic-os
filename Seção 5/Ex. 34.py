"""Exercício 34

Ler nota do aluno e devolver a classificação.

"""

nota = float(input('Inserir a nota do aluno: '))
faltas = int(input('Número de faltas do aluno: '))

if faltas > 20:
    if nota <= 3.9:
        print('Conceito: E')
    elif nota > 3.9 and nota <= 4.9:
        print('Conceito: E')
    elif nota > 4.9 and nota <= 7.4:
        print('Conceito: D')
    elif nota > 7.4 and nota <= 8.9:
        print('Conceito: C')
    elif nota > 8.9:
        print('Conceito: B')
else:
    if nota <= 3.9:
        print('Conceito: E')
    elif nota > 3.9 and nota <= 4.9:
        print('Conceito: D')
    elif nota > 4.9 and nota <= 7.4:
        print('Conceito: C')
    elif nota > 7.4 and nota <= 8.9:
        print('Conceito: B')
    elif nota > 8.9:
        print('Conceito: A')
