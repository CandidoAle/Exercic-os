"""Exercício 50


- Chico = 1.5 - Cresce 0.2 / ano
- Zé 0 1.1 - Cresce 0.3 / ano
- Em quantos anos Zé alcança Chico

"""

Chico = 1.5
Zé = 1.1
ano = 0

while True:
    Chico = Chico + 0.2
    Zé = Zé + 0.3
    ano += 1

    if Chico <= Zé:
        break

print(f'Altura Chico: {Chico}')
print(f'Altura Zé: {Zé}')
print(f'Quanto tempo levou: {ano} anos')