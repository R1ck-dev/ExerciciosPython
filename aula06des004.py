#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e
# todas as informações possíveis sobre ele

# Solicita ao usuário que insira um valor e armazena na variável 'num' como string
num = input('Digite um valor qualquer: ')

# Exibe o valor digitado pelo usuário
print(f'Valor digitado é {num}.')

# Mostra o tipo primitivo do valor digitado (sempre será 'str', pois input retorna uma string)
print(f'O tipo do valor é {type(num)}')

# Verifica se o valor digitado contém apenas números
print(f'[{num}] é numérico? R: {num.isnumeric()}')

# Verifica se o valor digitado contém apenas letras
print(f'[{num}] é alfabético? R: {num.isalpha()}')

# Verifica se o valor digitado contém letras e/ou números
print(f'[{num}] é alpha-numérico? R: {num.isalnum()}')

# Verifica se todas as letras do valor digitado estão em minúsculas
print(f'[{num}] está em minúsculo? R: {num.islower()}')

# Verifica se todas as letras do valor digitado estão em maiúsculas
print(f'[{num}] está em maiúsculo? R: {num.isupper()}')

# Verifica se a primeira letra do valor digitado está em maiúscula e o restante em minúscula
print(f'[{num}] está capitalizada? R: {num.istitle()}')
