"""Exercício 27

- H(n) = 1/1 + 1/2 + 1/3 + ... + 1/n
- Ler n e calcular H(n)

"""

n = int(input('Inserir número: '))
n_cont = 1
soma = 0

while n_cont <= n:
    soma = soma + 1/n_cont
    n_cont += 1

print(f'Resultado da série harmônica: {soma}')