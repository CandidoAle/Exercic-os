"""Exercício 60

- Ler vários números (interromper quando 0 for digitado).
- Imprimit a soma, a quantidade, a média, o maior, o menor, e a média dos pares
"""

lista_num = []

while True:
    num = float(input('Inserir número: '))
    if num == 0:
        break
    else:
        lista_num.append(num)

soma = sum(lista_num)
quantidade = len(lista_num)
media = soma / quantidade
maior = max(lista_num)
menor = min(lista_num)

soma_pares = 0

for n in lista_num:
    if n % 2 == 0:
        soma_pares = soma_pares + n

print(f'A soma dos números digitados: {soma}')
print(f'A quantidade de números digitados: {quantidade}')
print(f'A média dos números digitados: {media}')
print(f'O maior número digitado: {maior}')
print(f'O menor número digitado: {menor}')
print(f'A soma dos pares: {soma_pares}')