"""Exercício 17

Receber parametros do trpézio

Devolver área e não adimiter que Bmaior ou Bmenor sejam <= 0
"""

altura = float(input('Inserir altura do trapézio: '))
bmaior = float(input('Inserir comprimento da base maior: '))
bmenor = float(input('Inserir comprimento da base menor: '))

while bmaior <= 0 or bmenor <=0:
    if bmaior <=0:
        print('Base maior não pode ser menor ou igual a 0.')
        bmaior = float(input('Inserir comprimento da base maior: '))
    if bmenor <= 0:
        print('Base menor não poder ser menor ou igual a zero.')
        bmenor = float(input('Inserir comprimento da base menor: '))

volume = (bmaior + bmenor) * altura * 0.5

print(f'Altura: {altura}')
print(f'Base Maior: {bmaior}')
print(f'Base Menor: {bmenor}')
print(f'O volume do Trapézio é {volume}')
