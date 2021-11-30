"""Exercício 52

- Fornecer valor do saque
- Devolver menor quantidade de notas possíveis usando as notas 100, 50, 20, 10, 5, 2 e 1

"""

# valor_saque = int(input('Inserir valor do saque: '))
valor_saque = 278
contagem_notas = {100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0}
notas_disponiveis = (100, 50, 20, 10, 5, 2, 1)
cont_notas = 0
i = 0


while valor_saque != 0:

    if valor_saque - notas_disponiveis[i] >= 0:
        valor_saque = valor_saque - notas_disponiveis[i]
        cont_notas += 1
        contagem_notas[notas_disponiveis[i]] = cont_notas
        print(valor_saque)

    else:
        i += 1
        cont_notas = 0

for registro in contagem_notas:
    if contagem_notas[registro] > 0:
        print(f'{contagem_notas[registro]} notas de {registro}')