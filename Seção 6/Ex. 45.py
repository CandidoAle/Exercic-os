"""Exercício 45

- Faça um programa que converta km/h para m/s e vice versa.
- Usuário escolhe o que ele quer.
- Usuário pode fazer quantas conversões quiser até a opção de finalizar for escolhida
"""

while True:
    print("1 - Converter km/h para m/s")
    print("2 - Converter m/s para km/h")
    print("3 - Finalizar programa")
    while True:
        escolha = int(input('Escolha a opção desejada: '))
        if escolha != 1 and escolha != 2 and escolha != 3:
            print('Opção invalida.')
            escolha = int(input('Escolha a opção desejada: '))
        else:
            break
    if escolha == 3:
        break
    dado = float(input('Inserir dado a ser convertido: '))
    if escolha == 1:
        conv = dado * 0.27777778
        print(f'{dado} km/h equivale a {conv} m/s')
    elif escolha == 2:
        conv = dado * 3.6
        print(f'{dado} m/s equivale a {conv} km/h')