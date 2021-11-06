"""Exercício 15

Usar Switch para sortear um numero de 1 a 7 e imprimir o dia correspondente a esse número
"""

dia = int(input('Qual dia da semana? (1 a 7) '))

while dia < 1 or dia > 7:
    print('Por favor, escolher um número entre 1 e 7')
    dia = int(input('Qual dia da semana? (1 a 7) '))

semana = ['Domingo', 'Segunda-Feira', 'Terça-Feira', 'Quarta-Feira', 'Quinta-Feira', 'Sexta-Feira', 'Sábado']

print(f'O dia que você escolheu é {semana[dia - 1]} ')