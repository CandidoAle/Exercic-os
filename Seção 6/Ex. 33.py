"""Exercício 33

- Receber três números: n, num1 e num2
- Imprimir os 6 primeiros multiplos de num1, num2 ou ambos maiores que zero

"""

n = int(input('Inserir número de multiplos que você quer: '))

if n <= 0:
    while n <= 0:
        print('Este número deve ser maior do que zero.')
        n = int(input('Inserir número de multiplos que você quer: '))

num1 = int(input('Insira o primeiro número: '))

if num1 <= 0:
    while num1 <= 0:
        print('Este número deve ser maior do que zero.')
        num1 = int(input('Insera o primeiro número: '))

num2 = int(input('Insira o segundo número: '))

if num2 <= 0:
    while num2 <= 0:
        print('Este número deve ser maior do que zero.')
        num2 = int(input('Insera o segundo número: '))

num_teste = 0
multilplos = []

while len(multilplos) < n:
    if num_teste % num1 == 0 or num_teste % num2 == 0:
        multilplos.append(num_teste)
    num_teste += 1

print(f'Os {n} primeiros multiplos de {num1} e {num2} são: {multilplos}')