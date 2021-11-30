"""Exercício 6

Ler 10 inteiros e imprimir a média

"""

lista = []
tamanho_lista = len(lista)

while tamanho_lista <= 9:
    numx = int(input('Adicionar número para contagem: '))
    lista.append(numx)
    tamanho_lista = len(lista)

soma = sum(lista)
média = soma/10
print(f'A média calculada é {média}')