"""Exercício 11

Receber um número

Verificar se é maior que zero -> Caso sim, devolver 'Número invalido'

Caso não -> Devolver a soma dos algarismos
"""

numero = input('Inserir número: ')
soma = 0
tamanho_while = len(numero) - 1
i = 0

if int(numero) < 0:
    print(f'Número {numero} é invalido não é maior que zero.')
else:
    while i <= tamanho_while:
        soma = soma + int(numero[i])
        i = i + 1
    print(f'A soma dos algarismos do número é {numero} é {soma}')