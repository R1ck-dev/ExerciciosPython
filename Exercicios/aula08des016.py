# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

# Importa a função 'floor' do módulo math para arredondar para baixo
from math import floor

# Solicita ao usuário que insira um número real e armazena na variável 'num'
num = float(input('Digite um numero real qualquer: '))

# Exibe a porção inteira do número, utilizando a função 'floor' para arredondar para baixo
print('{}'.format(floor(num)))
