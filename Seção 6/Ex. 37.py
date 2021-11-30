"""Exercício 37

- Verificar quais números entre 1000 e 9999 obedecem a lei:
        ABCD
        (AB + CD) ** 2 = ABCD
"""

lim_inf = 1000
lim_sup = 9999

while lim_inf <= lim_sup:
    lim_inf_str = str(lim_inf)
    part_alta = int(lim_inf_str[0:2])
    part_baixa = int(lim_inf_str[2:4])
    comparativo = (part_alta + part_baixa) ** 2

    if comparativo == lim_inf:
        print(lim_inf)

    lim_inf += 1