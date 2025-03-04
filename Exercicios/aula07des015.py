# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

# Solicita ao usuário a quantidade de quilômetros rodados e armazena na variável 'qtd_km'
qtd_km = float(input('Informe a quantidade de Km rodados: '))

# Solicita ao usuário a quantidade de dias que o carro foi alugado e armazena na variável 'qtd_dias'
qtd_dias = int(input('Informe a quantidade de dias em que o carro foi alugado: '))

# Calcula o custo referente à quilometragem percorrida (R$ 0,15 por km)
pre_km = qtd_km * 0.15

# Calcula o custo referente aos dias alugados (R$ 60 por dia)
pre_dias = qtd_dias * 60

# Calcula o preço final somando os valores de quilometragem e diárias
pre_final = pre_km + pre_dias

# Exibe os detalhes do aluguel e o valor total a ser pago
print(f'O carro foi alugado por {qtd_dias} dias, e percorreu {qtd_km}km', end='')
print(', portanto a soma se refere a R$ {} (dias usados) e R${:.2f} (km percorridos)'.format(pre_dias, pre_km), end=' ')
print('resultando no preço final de R${:.2f}'.format(pre_final))
