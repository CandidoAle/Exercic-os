"""Exercício 1

- Programa que motre os 5 primeiros números multiplos de 3 maiores que zero.

"""

num = 0
lista = []
tamanho_lista = len(lista)

while tamanho_lista != 5:

    if num % 3 == 0 and num > 0:
        lista.append(num)

    num += 1
    tamanho_lista = len(lista)

print(f' 5 primeiros números multiplos de 3 maiores que zero: {lista}')