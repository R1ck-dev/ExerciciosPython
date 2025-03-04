# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

# Solicita ao usuário que insira um valor em metros e armazena na variável 'num'
num = int(input('Digite um valor qualquer em METROS: '))

# Converte o valor de metros para centímetros (1 metro = 100 cm)
cent = num * 100

# Converte o valor de centímetros para milímetros (1 cm = 10 mm)
mili = cent * 10

# Exibe a conversão de metros para centímetros
print(f'[{num} metros] equivale a {cent} centímetros')

# Exibe a conversão de metros para milímetros
print(f'[{num} metros] equivale a {mili} milimetros')
