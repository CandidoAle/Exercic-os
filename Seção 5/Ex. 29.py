""""
Exercício 29

Prova de matemática
5 perguntas de soma de números aleatórios.

Ao final - imprimir respostas do aluno, respostas corretas e nota.
"""
import random

num1 = random.randint(1,101)
num2 = random.randint(1,101)
num3 = random.randint(1,101)
num4 = random.randint(1,101)
num5 = random.randint(1,101)
num6 = random.randint(1,101)
num7 = random.randint(1,101)
num8 = random.randint(1,101)
num9 = random.randint(1,101)
num10 = random.randint(1,101)
numeros1 = [num1, num3, num5, num7, num9]
numeros2 = [num2, num4, num6, num8, num10]
gabarito = [num1 + num2, num3 + num4, num5 + num6, num7 + num8, num9 + num10]
res = []
nota = 0


for i in range(1,6):
    res_aluno = int(input(f'{numeros1[i-1]} + {numeros2[i-1]} = '))
    res.append(res_aluno)
    if res_aluno == gabarito[i-1]:
        nota = nota + 2.0

print('Respostas do Aluno e Gabarito: ')
print(res)
print(gabarito)
print(f'Nota do Aluno {nota}')