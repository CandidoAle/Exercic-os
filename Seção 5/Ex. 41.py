"""Exercício 41

- Ler IMC
- Devolver diagnóstico

"""

imc = float(input('Inserir IMC: '))

if imc < 18.5:
    print(f'{imc} é considerado Abaixo do Peso. ')
elif 18.5 <= imc < 24.9:
    print(f'{imc} é considerado Saudável. ')
elif 24.9 <= imc < 29.9:
    print(f'{imc} é considerado Peso em Excesso. ')
elif 29.9 <= imc < 34.9:
    print(f'{imc} é considerado Obesidade Grau I. ')
elif 34.9 <= imc < 39.9:
    print(f'{imc} é considerado Obesidade Grau II (Severa). ')
elif imc > 39.9:
    print(f'{imc} é considerado Obsesidade Grau III (Mórbida). ')

