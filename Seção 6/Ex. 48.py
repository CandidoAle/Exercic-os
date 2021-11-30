"""Exercício 48

- Somar termos pares da sequência de Fibonacci
- Não exceder 4.000.000

"""

Fibonacci = [0, 1]
Fibonacci_Pares = []
indice = 0

while sum(Fibonacci_Pares) < 4000000:
    add_Fibonacci = Fibonacci[indice] + Fibonacci[indice + 1]
    Fibonacci.append(add_Fibonacci)

    if add_Fibonacci % 2 == 0:
        Fibonacci_Pares.append(add_Fibonacci)

    if sum(Fibonacci_Pares) > 4000000:
        Fibonacci_Pares.pop()
        break

    indice += 1

soma_fbpar = sum(Fibonacci_Pares)
print(f'Soma dos Fb pares = {soma_fbpar}')