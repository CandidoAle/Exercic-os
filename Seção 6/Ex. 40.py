"""Exercício 40

- Achar a, b, c para a + b + c = 1000. Obedecendo que a ** 2 + b ** 2 = c ** 2
"""
from random import randint

while True:
    a = randint(1, 1000)
    b = randint(1, 1000)
    c = (a ** 2 + b ** 2) ** 0.5

    if a + b + c == 1000:
        break

print(a)
print(b)
print(c)

a = 1

while True:
    b = int((2000 * a - 1000 ** 2) / (2 * a - 2000))
    c = int(1000 - a - b)

    if a + b + c == 1000 and a ** 2 + b ** 2 == c ** 2:
        break
    a += 1

print(a)
print(b)
print(c)

