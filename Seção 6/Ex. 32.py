"""Exercício 32

- Simular o lançamento de dois dados n vezes.
- Devolver a relação entre eles (> < ou =)
"""

from random import randint

# n = int(input('Quantas vezes você quer lançar o dado? '))
n = 10000000
cont_vezes = 1
ind = 0

while cont_vezes <= n:
    dado1 = randint(1,6)
    dado2 = randint(1,6)
    print(f'Os dados tiveram os resultados: D1 = {dado1} e D2 = {dado2}')
    if dado1 == dado2:
        print('Os dados são iguais')
        ind += 1
    elif dado1 > dado2:
        print('D1 é maior que D2.')
    elif dado1 < dado2:
        print('D2 é maior que D1.')
    cont_vezes += 1

real = ind/n * 100
print(real)
