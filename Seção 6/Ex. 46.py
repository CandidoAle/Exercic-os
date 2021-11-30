"""Exercício 46

- Gerar um número aleatório de 1 a 1000
- Usuário deve tentar acertar o número gerado
- Contar tentativas do usuário

"""
from random import randint

numero = randint(1,1000)
tentativas = 0
print(numero)

while True:
    chute = int(input('Qual número foi sorteado? '))
    tentativas += 1
    if chute == numero:
        break

print(f'Resposta: {numero}')
print('Você acertou!')
print(f'Você fez {tentativas} tentativas.')