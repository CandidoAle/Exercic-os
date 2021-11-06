"""Exercício 14

Notas do Aluno:
lab - 2
ava - 3
exa - 5

0 - 2.9 - Reprovado
3 - 4.9 - Recuperação
5 - 10 - Aprovado
"""

lab = float (input('Inserir nota de Laboratório: '))
if lab >= 0 and lab <= 10:
    ava = float(input('Inserir nota de Avaliação: '))
    if ava >= 0 and ava <= 10:
        exa = float(input('Inserir nota de Exame Final: '))
        if exa >= 0 and exa <= 10:
            media = 0.2 * lab + 0.3 * ava + 0.5 * exa
            print(f'Média final do aluno é {media}')
            if media <= 2.9:
                print('Resultado: Reprovado')
            elif media <= 4.9:
                print('Resultado: Recuperação')
            elif media > 4.9:
                print('Resultado: Aprovado')
        else:
            print('Nota do exame deve estar entre 0 e 10.')
    else:
        print('Nota da avaliação deve estar entre 0 e 10')
else:
    print('Nota do trabalho de laboratório deve estar entre 0 e 10')

