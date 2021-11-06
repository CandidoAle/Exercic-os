"""Exercício 10

Receber sexo e altura de um usuário e devolver seu peso ideal.

Formula: Masculino - 72.7 * h - 58        Feminino - 62.1 * h - 44.7
"""

sexo = input('Qual o seu sexo? (Masculino/Feminino): ')
altura = float(input('Qual a sua altura? '))

if sexo == 'Masculino':
    peso_ideal = 72.7 * altura - 58
else:
    peso_ideal = 62.1 * altura - 44.7

print(f'Seu peso ideal é {peso_ideal}')

