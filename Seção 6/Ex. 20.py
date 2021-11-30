"""Exercício 20

- Ler sequência de números inteiros.
- Informar número de dados lidos
- Informar quantos números são pares
- o processo termina quando número de entrada for 1000

"""

dados = []
registrar = int(input('Registrar número: '))
dados.append(registrar)

while registrar != 1000:
    registrar = int(input('Registrar próximo número: '))
    if registrar != 1000:
        dados.append(registrar)

cont = 0

for numero in dados:
    if numero % 2 == 0:
        cont += 1

qtd_dados = len(dados)

print(f'Você registrou {qtd_dados} dados.')
print(f'{cont} desses dados são pares')