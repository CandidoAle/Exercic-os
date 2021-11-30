"""Exercício 36

- Calcular a soma dos quadrados dos números de 1 a 100
- Calcular o quadrado da soma dos números de 1 a 100
"""

num = 100
soma = 0
soma_quadrados = 0
cont = 1

while cont <= num:
    soma = soma + cont
    soma_quadrados = soma_quadrados + cont ** 2
    cont += 1

quadrado_soma = soma ** 2

print(f'A soma dos quadrados é: {soma_quadrados}')
print(f'O quadrado da soma é: {quadrado_soma}')

