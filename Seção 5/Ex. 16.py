"""Exercício 16

Usar Switch para sortear um numero de 1 a 12 e imprimir o mês correspondente a esse número
"""

mes = int(input('Qual dia da semana? (1 a 12) '))

while mes < 1 or mes > 12:
    print('Por favor, escolher um número entre 1 e 7')
    mes = int(input('Qual dia da semana? (1 a 7) '))

ano = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']

print(f'O dia que você escolheu é {ano[mes - 1]} ')