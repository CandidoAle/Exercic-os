"""Exercício 31

- Programa que calcule o valor da sequência S

    S = 1/1 + 3/2 + 5/3 + 7/4 + ... + 99/50

"""

numerador = 1
numeradores = []

denominador = 1
denominadores = []

while denominador <= 50:
    denominadores.append(denominador)
    denominador += 1

while numerador <= 99:
    if numerador % 2 !=0:
        numeradores.append(numerador)
    numerador += 1

soma = 0
for elemento in denominadores:
    parc = numeradores[elemento -1]/elemento
    soma = soma + parc

print(soma)