"""Exercício 22

Ler idade e tempo de serviço do trabalhador
Devolver se ele pode ou não se aposentar

"""

idade = int(input('Idade do trabalhador: '))
tempo_serv = int(input('Tempo de serviço do trabalhador: '))

if idade >= 65 or tempo_serv >= 30 or (idade >= 60 and tempo_serv >= 25):
    print('Pode se aposentar.')
else:
    print('Não pode se aposentar.')