"""
Exercício 5
Verificar se notas são validas
Fazer a média de duas notas
"""

P1 = float(input('Inserir nota da P1: '))

if P1 < 0 or P1 > 10:
    print(f'Nota {P1} é invalida. Programa encerrado')
else:
    P2 = float(input('Inserir nota da P2: '))
    if P2 < 0 or P2 > 10:
        print(f'Nota {P2} é invalida. Programa encerrado')
    else:
        media = (P1 + P2) / 2
        print(f'A média do aluno é {media}')
