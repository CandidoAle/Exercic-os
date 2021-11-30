"""Exercício 58

- Somar números primos entre a e b fornecidos pelo usuário
"""

num1 = int(input('Inserir número 1: '))
num2 = int(input('Inserir número 2: '))

lim_inf = num1
soma = 0

while True:

    if lim_inf == 1:
        contador = 1
    else:
        contador = lim_inf - 1

    while True:

        if contador == 1:
            soma = soma + lim_inf
            break
        elif lim_inf % contador == 0:
            break
        contador -= 1

    lim_inf += 1
    if lim_inf == num2:
        break

print(soma)