"""Exercício 43

- Receber número indeterminado de idades de indivíduos.
- Parar quando valor fornecido por zero
- Calcular média do grupo

"""

num_pessoas = 0
idades = []

while True:
    idade = int(input(f'Inserir idade do indíviduo {num_pessoas + 1}: '))
    if idade == 0:
        break
    idades.append(idade)
    num_pessoas += 1

print(f'Lista de idades: {idades}')
media_idades = sum(idades)/len(idades)

print(f'A média das idades dos índividuos é: {media_idades}')
