"""Exercício 17

- Ler número inteiro positivo (N)
- Calcular a soma dos números de 0 até N
"""

N = int(input('Inserir número: '))
cont = 0
soma = 0

while N < 0:
    print('O número deve ser positivo.')
    N = int(input('Inserir número: '))

while cont <= N:
    soma = soma + cont
    cont += 1

print(f'A soma dos {N} primeiros números é {soma}')