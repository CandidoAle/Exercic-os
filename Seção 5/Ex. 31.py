"""Exercício 31

Receber peso e altura de uma pessoa.
Devolver classificação conforme a tabela.
"""

altura = float(input('Inserir altura: '))
peso = float(input('Inserir peso: '))

if altura < 1.20:
    if peso < 60:
        print('Classificação A')
    elif peso >= 60 and peso <= 90:
        print('Classificação D')
    else:
        print('Classificação G')

if altura >= 1.20 and altura <= 1.70:
    if peso < 60:
        print('Classificação B')
    elif peso >= 60 and peso <= 90:
        print('Classificação E')
    else:
        print('Classificação H')

if altura > 90:
    if peso < 60:
        print('Classificação C')
    elif peso >= 60 and peso <= 90:
        print('Classificação F')
    else:
        print('Classificação I')