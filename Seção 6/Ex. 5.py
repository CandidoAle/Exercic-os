"""Exercício 6

Ler 10 inteiros e imprimir a soma

"""

lista = []
tamanho_lista = len(lista)

while tamanho_lista <= 9:
    numx = int(input('Adicionar número para contagem: '))
    lista.append(numx)
    tamanho_lista = len(lista)

soma = sum(lista)
print(f'A soma calculada é {soma}')