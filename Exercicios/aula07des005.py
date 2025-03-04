# Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.

# Solicita ao usuário que insira um número inteiro e armazena na variável 'num'
num = int(input('Digite um valor: '))

# Exibe o antecessor do número digitado, utilizando num - 1
# O argumento 'end = " "' mantém a próxima impressão na mesma linha
print(f'O valor antecessor de [{num}] é {num-1}', end=' ')

# Exibe o sucessor do número digitado, utilizando num + 1
print(f'e o valor sucessor é {num+1}')
