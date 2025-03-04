#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares
#ela pode comprar (consideranto US$1,00 = R$3,27)

# Solicita ao usuário que informe o valor disponível na conta e armazena na variável 'num'
num = float(input('Informe o valor existente na conta: '))

# Converte o valor em reais para dólares, considerando a taxa de câmbio de 1 dólar = 3.27 reais
dolar = num / 3.27

# Exibe o valor convertido para dólares, formatado com duas casas decimais
print('Com o seu valor na conta de [R$ {}], é possível converter para R$ {:.2f} doláres'.format(num, dolar))
