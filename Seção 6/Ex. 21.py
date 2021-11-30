"""Exercício 21

- Receber dois números
- Calcular e devolver a soma dos números pares entre eles
- Calcular e devolver a mutiplicação dos ímpares entre eles
"""

num1 = int(input('Inserir primeiro número: '))
num2 = int(input('Inserir segundo número: '))
soma = 0
multiplicacao = 1

for num in range(num1,num2 + 1):
    if num % 2 == 0:
        soma = soma + num
    else:
        multiplicacao = multiplicacao * num

print(f'A soma dos pares: {soma}')
print(f'A multiplicação dos impares: {multiplicacao}')

