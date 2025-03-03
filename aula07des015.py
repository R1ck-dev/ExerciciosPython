qtd_km = float(input('Informe a quantidade de Km rodados: '))
qtd_dias = int(input('Informa a quantidade de dias em que o carro foi alugado: '))
pre_km = qtd_km*0.15
pre_dias = qtd_dias*60
pre_final = pre_km+pre_dias
print(f'O carro foi alugado por {qtd_dias} dias, e percorreu {qtd_km}km', end='')
print(', portanto a soma se refere a R$ {} (dias usados) e R${:.2f} (km percorridos)'.format(pre_dias, pre_km), end=' ')
print('resultando no preço final de R${:.2f}'.format(pre_final))