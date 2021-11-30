"""Exercício 9

Ler N inteiros e imprimir só os impares

"""

num_numeros = int(input('Quantos números você vai colocar no conjunto? '))
lista = []
lista_impar = []
tamanho_lista = len(lista)

while tamanho_lista <= (num_numeros - 1):
    numx = int(input('Adicionar número para contagem: '))
    lista.append(numx)

    if numx % 2 != 0:
        lista_impar.append(numx)

    tamanho_lista = len(lista)

print(f'Os números ímpares do conjunto são {lista_impar}')