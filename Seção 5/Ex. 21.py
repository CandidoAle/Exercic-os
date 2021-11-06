"""Exercício 21
Usuário escolhe a operação matemática que deseja realizar
Usuário insere dois números

Programa devolve a operação=
"""

print('Operações disponíveis:')
print('Adição = A')
print('Subtração = S')
print('Multiplicação = M')
print('Divisão = D')

op = input('Qual operação deseja realizar? A, S, M ou D? ')

while op !='A' and op !='S' and op !='M' and op !='D':
    op = input('Favor escolher uma das operações a seguir: A, S, M ou D ')

num1 = float(input('Inserir primeiro número: '))
num2 = float(input('Inserir segundo número: '))

if op == 'A':
    resultado = num1 + num2
    print(f'O resultado é: {resultado}')
elif op == 'S':
    resultado = num1 - num2
    print(f'O resultado é: {resultado}')
elif op == 'M':
    resultado = num1 * num2
    print(f'O resultado é: {resultado}')
elif op == 'D':
    resultado = num1 / num2
    print(f'O resultado é: {resultado}')