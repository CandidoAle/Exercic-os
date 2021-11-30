"""Exercício 44

- Ler número do usuário
- Imprimir sequencia de Fibonacci até o primeiro superior ao número lido
"""

num = int(input('Inserir número: '))
Fibonacci = [0, 1]
indice = 0

while Fibonacci[-1] < num:
    add_Finonacci = Fibonacci[indice + 1] + Fibonacci[indice]
    Fibonacci.append(add_Finonacci)
    indice += 1

print(Fibonacci)


