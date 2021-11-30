"""Exercício 22

- Ler valores de 10 a 20. (Quantos o usuários quiser)
- O input encerra quando o usuário declarar algo fora dos limites (10 a 20)
- Fornecer a média desses valores.

"""

lista = []
num = float(input('Insira o número:  '))
lista.append(num)

while num >= 10 and num <= 20:
    num = float(input('Insira o número: '))
    lista.append(num)

lista.pop()

soma = sum(lista)
media = soma / len(lista)

print(f'A média é: {media}')