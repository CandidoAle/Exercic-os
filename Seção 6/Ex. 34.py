"""Exercício 34

- Achar Minimo divisor comum para os números de 1 a 20
"""

num = 1
num_teste = 1

while num != 10:
    teste = num_teste % num
    if teste == 0:
        num += 1
    else:
        num_teste += 1
        num = 1

print(num_teste)