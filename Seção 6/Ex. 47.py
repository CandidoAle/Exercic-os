"""Exercício 47

- Menu com as opções:

    1 - Adição
    2 - Subtração
    3 - Multiplicação
    4 - Divisão
    5 - Saída

- Ler dois números
- Mostrar o resultado para o usuário e voltar para o menu

"""

while True:
    print('1 - Adição')
    print('2 - Subtração')
    print('3 - Multiplicação')
    print('4 - Divisão')
    print('5 - Saída')
    opcao = int(input('Escolha uma das opções acima: '))

    while opcao < 1 or opcao > 5:
        print('Opção invalida')
        opcao = opcao = int(input('Escolha uma das opções do menu: '))

    if opcao == 5:
        break

    num1 = float(input('Inserir número 1: '))
    num2 = float(input('Inserir número 2: '))

    if opcao == 1:
        resposta = num1 + num2
    if opcao == 2:
        resposta = num1 - num2
    if opcao == 3:
        resposta = num1 * num2
    if opcao == 4:
        resposta = num1 / num2

    print(f'A resposta para a operação {opcao} é {resposta}')
