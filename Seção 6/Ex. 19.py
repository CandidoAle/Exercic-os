"""Exercício 19

- Ler número entre 100 e 999
- Imprimir cada algarismo que compoe o numero
"""

num = int(input('Inserir número: '))

while num < 100 or num > 999:
    print('O número deve estar entre 100 e 999.')
    num = int(input('Inserir número: '))

num = str(num)

for algarismo in num:
    print(algarismo)