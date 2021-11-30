"""Exercício 18

- Ler uma quantidade N de número.
- Imprimir o maior deles
- Imprimir quantas vezes o maior foi fornecido
"""

N = int(input('Quantos números você quer registrar: '))
numeros = []
tamanho = len(numeros)

while tamanho < N:
    elemento = int(input('Inserir número: '))
    numeros.append(elemento)
    tamanho = len(numeros)

maior = max(numeros)
print(f'O maior número da lista é {maior}')

cont = 0

for numero in numeros:
    if numero == maior:
        cont += 1

print(f'Esse número foi registrado {cont} vezes.')