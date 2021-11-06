"""Exercício 19 (46)

Ler um número de 3 digitos e inverter.
Exemplo: Ler 123 e devolver 321
"""

numero = input('Digitar número com 3 digitos: ')

lista = numero.split()

if len(numero) != 3:
    print('O número deve conter 3 dígitos.')
else:
    invertido = numero[::-1]
    print(invertido)
