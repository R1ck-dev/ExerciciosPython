from des_moedas import aula22des108
from des_moedas import aula22des109

def resumo(valor, aum, des):
    print('-' *30)
    print(f'{"Resumo do Valor":^30}')
    print('-' * 30)
    print(f'{"Preço Analisado:":<18} R${aula22des108.formatar(valor):>10}')
    print(f'{"Dobro do Preço:":<18} R${aula22des109.dobro(valor, True):>10}')
    print(f'{"Metade do Preço:":<18} R${aula22des109.metade(valor, True):>10}')
    print(f'{aum}% de aumento:'.ljust(18), f'R${aula22des109.aumentando(valor, aum, True):>10}')
    print(f'{des}% de desconto:'.ljust(18), f'R${aula22des109.diminuindo(valor, des, True):>10}')
    print('-' * 30)
    return