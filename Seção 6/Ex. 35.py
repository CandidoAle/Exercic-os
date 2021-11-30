"""Exercício 35

-  Ler dois valores fornecidos pelo usuário.
- Somar os números impares contidos no intervalo definido
"""

num1 = int(input('Primeiro número: '))
num2 = int(input('Segundo número: '))

intervalo = sorted([num1, num2])

lim_inf = intervalo[0]
lim_sup = intervalo[1]
soma = 0

while lim_inf <= lim_sup:
    if lim_inf % 2 != 0:
        soma = soma + lim_inf
    lim_inf += 1

print(f'A soma deste intervalo é {soma}')
