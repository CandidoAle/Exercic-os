"""Exercício 10

- soma dos 50 primeros números pares maiores que zero
"""

lista_numeros = []
tamanho_lista = len(lista_numeros)
num = 1

while tamanho_lista < 50:

    if num % 2 == 0:
        lista_numeros.append(num)
        tamanho_lista = len(lista_numeros)

    num += 1

soma = sum(lista_numeros)
print(f'A soma dos 50 primeiros números pares maiores que zero é {soma}')