from utilidadescev.moeda.calc_valores import metade, dobro, aumentando, diminuindo
from utilidadescev.moeda.formatar import formatar
def resumo(valor, aum, des):
    print('-' *30)
    print(f'{"Resumo do Valor":^30}')
    print('-' * 30)
    print(f'{"Preço Analisado:":<18} R${formatar(valor):>10}')
    print(f'{"Dobro do Preço:":<18} R${dobro(valor, True):>10}')
    print(f'{"Metade do Preço:":<18} R${metade(valor, True):>10}')
    print(f'{aum}% de aumento:'.ljust(18), f'R${aumentando(valor, aum, True):>10}')
    print(f'{des}% de desconto:'.ljust(18), f'R${diminuindo(valor, des, True):>10}')
    print('-' * 30)
    return