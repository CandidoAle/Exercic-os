"""Exercício 36

- Ler valor da venda
- Imprimir comissão do vendedor

"""

venda = float(input('Inserir valor da Venda: '))

if venda < 20000:
    comissao = 400 + 0.14 * venda
elif venda >= 20000 and venda < 40000:
    comissao = 500 + 0.14 * venda
elif venda >= 40000 and venda < 60000:
    comissao = 550 + 0.14 * venda
elif venda >= 60000 and venda < 80000:
    comissao = 600 + 0.14 * venda
elif venda >= 80000 and venda < 100000:
    comissao = 650 + 0.14 * venda
elif venda >= 100000:
    comissao = 700 + 0.16 * venda

print('O valor da comissão a ser paga é R$ %.2f' %comissao)
