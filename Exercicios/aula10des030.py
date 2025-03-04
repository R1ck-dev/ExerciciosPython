# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

# Solicita ao usuário um número inteiro e armazena na variável 'valor'
valor = int(input('Insira um valor qualquer: '))

# Verifica se o número é par ou ímpar
if valor % 2 == 0:  # Se o resto da divisão por 2 for 0, o número é par
    print('O valor é par!')
else:  # Caso contrário, o número é ímpar
    print('O valor é ímpar!')

# Exibe uma mensagem de finalização
print('\n---FIM---')
