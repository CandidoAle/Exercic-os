"""Exercício 59

- Escrever um programa que leia:
    num de habitantes na cidade
    valor do kwh

- Pra cada habitante
    consumo no mês
    código do consumidor = 1(Residencial), 2(Comercial) e 3(Industrial)

- Imprimir
    maior
    menor
    media
    consumo de cada categoria
"""

num_habitantes = int(input('Número de habitantes: '))
valor_kwh = float(input('Valor do kwh: '))

registro = 1
lista_consumo = []
lista_consumo_Res = []
lista_consumo_Com = []
lista_consumo_Ind = []

while registro != num_habitantes + 1:

    consumo = float(input(f'Quanto o consumidor {registro} consumiu?: '))
    lista_consumo.append(consumo)

    categoria = int(input('Qual a categoria de consumo? 1 - Res, 2 - Com ou 3 - Ind: '))
    if categoria == 1:
        lista_consumo_Res.append(consumo)
    elif categoria == 2:
        lista_consumo_Com.append(consumo)
    elif categoria == 3:
        lista_consumo_Ind.append(consumo)

    registro += 1

maior_consumo = max(lista_consumo)
menor_consumo = min(lista_consumo)
media = sum(lista_consumo) / num_habitantes

print(f'Maior consumo: {maior_consumo}')
print(f'Menor consumo: {menor_consumo}')
print(f'Consumo médio: {media}')

consumo_1 = sum(lista_consumo_Res)
consumo_2 = sum(lista_consumo_Com)
consumo_3 = sum(lista_consumo_Ind)

print(f'Consumo da categoria residencial: {consumo_1}')
print(f'Consumo da categorial comercial: {consumo_2}')
print(f'Consumo da categorial industrial: {consumo_3}')