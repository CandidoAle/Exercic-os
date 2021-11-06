"""
Exercício 27

Receber idade de um nadador

Devolver classificação - IA 5 a 7 - IB 8 a 10 - JA  11 a 13 - JB 14 a 17 - S 18+
"""

idade = int(input('Inserir idade do nadador: '))

if idade < 5:
    print('Deve ter pelo menos 5 anos para começar a natação.')
elif idade >= 5 and idade <= 7:
    print('Turma: Infantil A')
elif idade >= 8 and idade <= 10:
    print('Turma: Infantil B')
elif idade >= 11 and idade <= 13:
    print('Turma: Juvenil A')
elif idade >= 14 and idade <= 17:
    print('Turma: Juvenil B')
else:
    print('Turma: Sênior')