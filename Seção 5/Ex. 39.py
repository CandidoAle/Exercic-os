""" Exercício 39

- Ler salário atual do funcionário
- Ler tempo de serviço

"""

salario_atual = float(input('Inserir salário do funcionário: '))
tempo_servico = int(input('Inserir tempo de serviço: '))

# Reajuste

if salario_atual <= 500:
    salario_reajustado = salario_atual * 1.25
elif salario_atual > 500 and salario_atual <= 1000:
    salario_reajustado = salario_atual * 1.20
elif salario_atual > 1000 and salario_atual <= 1500:
    salario_reajustado = salario_atual * 1.15
elif salario_atual > 1500 and salario_atual <= 2000:
    salario_reajustado = salario_atual * 1.10
elif salario_atual > 2000:
    salario_reajustado = salario_atual
    print(f'Não terá reajuste por valor de salário.')

# Bonus

if tempo_servico < 1:
    print(f'Não elegível para bônus')
elif 1 <= tempo_servico <= 3:
    salario_reajustado = salario_reajustado + 100
elif 4 <= tempo_servico <= 6:
    salario_reajustado = salario_reajustado + 200
elif 7 <= tempo_servico <= 10:
    salario_reajustado = salario_reajustado + 300
elif tempo_servico > 10:
    salario_reajustado = salario_reajustado + 500

print(f'O salário para o funcionário será {salario_reajustado}')