"""Exercício 28

E = 1 + 1/1! + 1/2! + 1/3! + ... + 1/N!
- Receber N e calcular o resultado
"""
import math

N = int(input('Inserir número: '))
N_cont = 1
soma = 1

while N_cont <= N:
    fatorial = math.factorial(N_cont)
    soma = soma + 1/fatorial
    N_cont += 1


print(soma)