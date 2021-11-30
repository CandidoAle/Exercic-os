"""Exercício 55

- Calcular a soma de todos os números primos abaixo de 2.000.000
"""

n = 1000
soma = 0

while True:

    contador = n - 1

    while True:

        if contador == 1:
            soma = soma + n
            break

        elif n % contador == 0:
            break

        contador -= 1

    n -= 1

    if n == 1:
        soma = soma + 1
        break

print(soma)