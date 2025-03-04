# Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo:

# Define um dicionário com códigos ANSI para colorir a saída no terminal
cores = {'limpa':'\033[m', 'titulo':'\033[1;35m',
         'vermelho':'\033[31m', 'verde':'\033[32m', 'azul':'\033[34m'}

# Exibe um cabeçalho estilizado
print('-=*=-' * 10)
print(' ' * 18 , '{}EXERCICIO 63{}'.format(cores['titulo'], cores['limpa']))
print('-=*=-' * 10)

# Solicita ao usuário um número inicial
valor = int(input('Insira um valor qualquer: '))

# Inicializa variáveis de controle
cont = 0  # Contador de números inseridos
soma = 0  # Soma de todos os números inseridos

# Loop que continuará até o usuário inserir o valor 999 (condição de parada)
while valor != 999:
    cont += 1   # Incrementa o contador de números inseridos
    soma += valor  # Soma o valor atual ao total
    valor = int(input('Insira um valor qualquer: '))  # Solicita um novo valor

# Exibe o resultado final
print('Soma = {}\nContador = {}'.format(soma, cont))
