"""Exercício 61

- Algoritmo que ache o maior número palindromo feito do produto de dois números de 3 digitos.
- Números de 3 digitos = 100 a 999
999 * 999
999 * 998
999 * 997
...
999 * 100
998 * 999
"""

palíndromo = False

for i in range(999, 100, -1):
    for j in range(999, 100, -1):
        num = i * j
        num_text = str(num)
        if num_text[::] == num_text[::-1]:
            print(f'Palíndromo encontrado: {i} * {j} = {num}')
            palíndromo = True
            break
    if palíndromo == True:
        break


