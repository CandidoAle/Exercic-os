"""Exercício 49

- João = Carlos / 3
- Carlos faz aplicações em poupança - Rende 2 % ao mês
- João faz aplicação em renda fixa - Rende 5 % ao mês

"""

mes = 0
salario = 1

conta_carlos = 0
conta_joao = 0

rend_poup = 0.02
rend_rendf = 0.05

while True:
    conta_carlos = conta_carlos + salario
    conta_joao = conta_joao + salario / 3

    conta_carlos = conta_carlos * (1 + rend_poup)
    conta_joao = conta_joao * (1 + rend_rendf)

    mes += 1
    print(f'Diferença entre as conta {conta_carlos - conta_joao}')

    if conta_carlos <= conta_joao:
        break

print(f'Saldo final Carlos = {conta_carlos}')
print(f'Saldo final João = {conta_joao}')
print(f'Número de meses até a equivalencia ou ultrapassagem = {mes}')

