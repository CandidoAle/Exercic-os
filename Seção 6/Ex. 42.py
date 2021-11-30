"""Exercício 42

- Ler vários valores e ir calculando o quadrado, o cubo e a raiz.
- Terminar o programa quando for fornecido um número zero ou negativo

"""

while True:
    num = float(input('Inserir número: '))
    if num <= 0:
        break
    print(f'O quadrado de {num} é {num ** 2}')
    print(f'O cubo de {num} é {num ** 3}')
    print(f'A raiz de {num} é {num ** 0.5}')

