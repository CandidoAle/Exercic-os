"""Exercício 8

Ler 10 inteiros e imprimir o maior e o menor número

"""

lista = []
tamanho_lista = len(lista)

while tamanho_lista <= 9:
    numx = int(input('Adicionar número para contagem: '))
    lista.append(numx)
    tamanho_lista = len(lista)

menor = min(lista)
maior = max(lista)
print(f'O maior número é {maior}')
print(f'O menor número é {menor}')