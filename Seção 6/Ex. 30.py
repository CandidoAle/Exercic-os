"""Exercício 30

- Ler um número n
- Calcular as seguintes sequências
    A - Sn = 1 + 2 + 3 + 4 + ... + n
    B - Sn = 1 - 2 + 3 - 4 + ... + [- (-1)^n * n]
    C - Sn = 1 + 3 + 5 + 7 + ... + nimpar
"""

# n = int(input('Inserir número))
n = 5
soma_sqA = 0
soma_sqB = 0

# Sequência A
n_cont = 1
while n_cont <= n:
    soma_sqA = soma_sqA + n_cont
    n_cont += 1

# Sequência B
n_cont = 1
while n_cont <= n:
    parc_sqB = (- (-1) ** (n_cont) * n_cont)
    soma_sqB = soma_sqB + parc_sqB
    n_cont += 1

# Sequência C
impares = []
tam_impares = 1
n_cont = 1

while tam_impares < n:
    if n_cont % 2 != 0:
        impares.append(n_cont)
        tam_impares = len(impares)
    n_cont += 1

soma_sqC = sum(impares)
print(impares)

print(f'Seq. A {soma_sqA}')
print(f'Seq. B {soma_sqB}')
print(f'Seq. C {soma_sqC}')

