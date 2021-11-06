"""Exercício 13

Ler 3 notas. A P1 e a P2 tem peso 1. A P3 tem peso 2.

Mostrar média
Mostrar aprovação ou reprovação. Critério de aprovação > 6.
 """

p1 = float(input('Inserir nota da P1: '))
p2 = float(input('Inserir nota da P2: '))
p3 = float(input('Inserir nota da P3: '))

if p1 >= 0 and p1 <= 10 and p2 >= 0 and p2 <= 10 and p3 >= 0 and p3 <= 10:

    media = 0.25 * p1 + 0.25 * p2 + 0.5 * p3
    print(f'A média do aluno é {media}')

    if media > 6:
        print('Aluno aprovado.')
    else:
        print('Aluno reprovado.')
else:
    print('Inserir só notas válidas')
