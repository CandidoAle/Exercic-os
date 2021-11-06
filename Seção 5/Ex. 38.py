"""Exercício 38

- Ler data de nascimento
- Checkar se a data é valida
"""

from datetime import date

# Dict de Meses

dias_meses = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
dias_meses_bissexto = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

# Leitura de data

data = input('Inserir data na forma dd/mm/aaa: ')

dia = int(data[0:2])
mes = int(data[3:5])
ano = int(data[6:12])

tamanho_data = len(data)

# Validando data

if tamanho_data !=10:
    print('Data fora do formato dd/mm/aaaa.')
elif mes < 1 or mes > 12:
    print('Mes invalido.')
elif ano % 4 == 0:
    if dia <= dias_meses_bissexto[mes]:
        print('Data válida')
    else:
        print(f'Data inválida. Esse mês possui {dias_meses_bissexto[mes]} dias.')
elif ano % 4 != 0:
    if dia <= dias_meses[mes]:
        print('Data válida')
    else:
        print(f'Data inválida. Esse mês possui {dias_meses[mes]} dias.')

# Calculando idade da pessoa

data_atual = date.today()

data_atual = str(data_atual)
ano_atual = int(data_atual[0:4])

total_ano = ano_atual - ano

print(f'Você tem {total_ano} anos')