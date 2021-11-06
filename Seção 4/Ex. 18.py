"""Exercício 18 (44)

Altura do degrau de uma escada - dado.
Altura desejada - dado
Devolver quantos degraus o usuário deve subir pra atingir a altura q ele quer.
"""
degrau = int(input('Qual a altura do degrau? '))
altura = int(input('Qual altura você deseja chegar? '))

num_degraus = altura // degrau

if degrau > altura:
    print('Degrau mais alto que a altura que você quer chegar.')
elif num_degraus * degrau == altura:
    print(f'Você deverá subir {num_degraus} para chegar a altura {num_degraus * degrau}.')
else:
    print(f'Você deverá subir {num_degraus} para chegar a altura {num_degraus * degrau}. Subindo mais um degrau você chegará a altura {(num_degraus+ 1) * degrau}')




