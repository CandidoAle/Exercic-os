"""Exercício 29

S(n) = 0 + 1/2! + 2/4! + 3/6! + ... + (n)/(n*2)!
- Receber número e calcular a série
"""
import math

n = int(input('Inserir número: '))
cont = 1
soma = 0

while cont <= n:
    fatorial = math.factorial(2 * cont)
    soma = soma + (cont)/(fatorial)
    cont += 1

print(soma)