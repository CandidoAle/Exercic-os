""" Exercício 37

- Ler horário de chegada e saída no estacionamento.
- Calcular quantidade de horas no estacionamento.
- Devolver valor a pagar e quantidade de horas.
"""
import math

hora_inicio = input('Inserir horário de entrada: ')
hora_fim = input('Inserir horário de saída: ')

minuto_hora_i = int(hora_inicio[3:5])
minuto_hora_f = int(hora_fim[3:5])
hora_hora_i = int(hora_inicio[0:2])
hora_hora_f = int(hora_fim[0:2])

minutos_totais = (minuto_hora_f - minuto_hora_i) + 60 * (hora_hora_f - hora_hora_i)
horas_pagas = math.ceil(minutos_totais/60)
cont = 0

if horas_pagas >= 5:
    cont = horas_pagas - 4
    valor = 2 * 1 + 2 * 1.40 + cont * 2
elif horas_pagas >= 3 and horas_pagas <= 4:
    cont = horas_pagas - 2
    valor = 2 * 1 + cont * 1.40
else:
    valor = horas_pagas * 1

print(f'Valor a ser pago R$ {valor} \n'
      f'Horas cobradas: {horas_pagas}')