"""Exercício 51

- Funcionário recebe aumento anual
    - 1995 - contratado por 2000
    - 1996 - +1.5 %
    - 1997 - 2 * +1.5%
    - 2021 - ??? Qual o salário

"""
salario = 2000
ano = 1995
aumento = 1.5 / 100

while ano < 2021:
    salario = salario * (1 + aumento)
    print(salario)
    aumento = 2 * aumento
    print(aumento)
    ano += 1
    print(ano)

print(f'O salário em {ano}: {salario}')