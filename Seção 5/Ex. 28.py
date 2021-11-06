"""Exercício 28

Receber 3 números e calcular as médias:
Geométricas
Ponderada
Harmonica
Aritimética
(A gosto do freguês)

"""

print('Qual média você deseja calcular? ')
print('G - Geométrica / P - Ponderada / H - Harmônica / A - Aritmética')
escolha = input('Escolher uma das opções acima: ')

while escolha != 'G' and escolha != 'P' and escolha != 'H' and escolha != 'A':
    print('Escolha apenas uma das abaixo.')
    print('G - Geométrica / P - Ponderada / H - Harmônica / A - Aritmética')
    escolha = input('Escolher uma das opções acima: ')

x = float(input('Número 1: '))
y = float(input('Número 2: '))
z = float(input('Número 3: '))

if escolha == 'G':
    media = (x * y * z) ** (1/3)
    print(f'A média aritimética é {media}.')
elif escolha == 'P':
    peso_x = float(input('Escolher peso para Número 1: '))
    peso_y = float(input('Escolher peso para Número 2: '))
    peso_z = float(input('Escolher peso para Número 3: '))
    while peso_x < 0 or peso_y < 0 or peso_z < 0:
        print('Os pesos devem ser números positivos.')
        peso_x = float(input('Escolher peso para Número 1: '))
        peso_y = float(input('Escolher peso para Número 2: '))
        peso_z = float(input('Escolher peso para Número 3: '))
    media = (peso_x * x + peso_y * y + peso_z * z) / (peso_x + peso_y + peso_z)
    print(f'A média ponderada é {media}.')
elif escolha == 'H':
    media = 1 / ((1/x) + (1/y) + (1/z))
    print(f'A média harmônica é {media}.')
elif escolha == 'A':
    media = (x + y + z)/3
    print(f'A média aritimética é {media}.')

