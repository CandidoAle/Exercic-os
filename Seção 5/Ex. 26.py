"""
Exercício 26

Ler km percorrido
Ler litros de comb usados

Calcular consumo - km/l
Classificar consumo em - 0 a 8 - Venda o Carro.
                         8 a 14 - Econômico
                         12 - Super economico
"""

km = float(input('Inserir quilometros percorridos: '))
l = float(input('Inserir litros de combustível consumido: '))

consumo = km / l

if consumo < 8:
    print('È melhor vender esse carro!')
elif consumo >= 8 and consumo < 14:
    print('Carro econômico.')
else:
    print('Carro Super econômico.')
