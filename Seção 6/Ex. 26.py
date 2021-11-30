"""Exercício 26

- Ler número.
- Encontrar primeiro múltiplo de 11, 13 e 17 após o número
"""

num = int(input('Inserir número: '))
multiplos = []
tam_multiplos = len(multiplos)

while tam_multiplos != 3:
    if num % 11 == 0 or num % 13 == 0 or num % 17 == 0:
        multiplos.append(num)
        tam_multiplos = len(multiplos)
    num += 1

print(f'Multiplos encontrados: {multiplos}')
