#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

# Solicita ao usuário que informe o preço do produto e armazena na variável 'num'
num = float(input('Informe o preço: '))

# Calcula o preço final aplicando um desconto de 5% (multiplicando por 0.05 e subtraindo do valor original)
preco_final = num - (num * 0.05)

# Exibe o preço final com o desconto, formatado com duas casas decimais
print('O preço final com o desconto de 5% é de R$ {:.2f}'.format(preco_final))
