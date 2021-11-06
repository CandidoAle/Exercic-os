"""
Exercício 20 (52)

Três amigos apostaram na loteria.
Valor do premio dividido proporcionalmente de acordo com o que cada um contribuiu

Ler - Valor do Prêmio
Ler - Valor de cada aposta

Devolver divisão
"""

# Entradas
premio = float(input('Inserir valor do prêmio: '))
aposta_1 = float(input('Inserir valor apostado pelo primeiro amigo: '))
aposta_2 = float(input('Inserir valor apostado pelo segundo amigo: '))
aposta_3 = float(input('Inserir valor apostado pelo terceiro amigo: '))

# Processamento

soma_aposta = aposta_1 + aposta_2 + aposta_3
parcela_1 = aposta_1 / soma_aposta
parcela_2 = aposta_2 / soma_aposta
parcela_3 = aposta_3 / soma_aposta

valor_1 = parcela_1 * premio
valor_2 = parcela_2 * premio
valor_3 = parcela_3 * premio

# Saída

print(f'Valor para o primeiro amigo R$ {valor_1}')
print(f'Valor para o primeiro amigo R$ {valor_2}')
print(f'Valor para o primeiro amigo R$ {valor_3}')

