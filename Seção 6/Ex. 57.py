"""Exercício 57

- Programa que calcule quantos números primos existem entre a e b
"""

num1 = int(input('Inserir número 1: '))
num2 = int(input('Inserir número 2: '))

lim_inf = num1
cont = 0

while True:

    if lim_inf == 1:
        contador = 1
    else:
        contador = lim_inf - 1

    while True:

        if contador == 1:
            cont += 1
            break
        elif lim_inf % contador == 0:
            break
        contador -= 1

    lim_inf += 1
    if lim_inf == num2:
        break

print(cont)