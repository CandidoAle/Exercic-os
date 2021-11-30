"""Exercício 53

- Ler um número n e imprimir um Triangulo de Floyd
"""

n = int(input('Inserir número: '))
num = 1
vezes = 1

for num1 in range(1, n + 1):
    lista = []

    for num2 in range(1, vezes + 1):
        lista.append(num)
        num += 1

    print(lista)
    vezes += 1

