"""Exercício 56

- Ler número inteiro n e calcular a soma dos n primeiros números primos
"""

while True:
    n = int(input('Inseir números de primos que vc quer calcular: '))
    if n > 0:
        break

num = 1
soma = 0
cont = 1

while True:

    if num == 1:
        contador = 1
    else:
        contador = num - 1

    while True:

        if contador == 1:
            soma = soma + num
            cont += 1
            break

        elif num % contador == 0:
            break
        contador -= 1

    if cont == n + 1:
        break

    num += 1

print(soma)
