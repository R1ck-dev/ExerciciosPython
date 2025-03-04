# Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.

# Dicionário contendo códigos ANSI para formatação de cores no terminal
cores = {'limpa':'\033[m', 'titulo':'\033[1;35m',
         'vermelho':'\033[31m', 'verde':'\033[32m', 'azul':'\033[34m'}

# Exibição do cabeçalho do exercício formatado com cores
print('-=*=-'*10)
print(' '*18 , '{}EXERCICIO 48{}'.format(cores['titulo'], cores['limpa']))
print('-=*=-'*10)

# Inicializa a variável 'soma' que armazenará a soma dos múltiplos de 3
soma = 0

# Loop que percorre os números de 1 a 500 (incluindo o 500)
for c in range (1, 501):
    if c % 2 != 0:  # Verifica se o número é ímpar
        if c % 3 == 0:  # Verifica se o número é múltiplo de 3
            # Exibe o número ímpar que é múltiplo de 3, formatado com cores
            print('{}{}{} é ímpar e múltiplo de 3'.format(cores['vermelho'], c, cores['limpa']))
            soma += c  # Adiciona o número à soma total

# Exibe o resultado final da soma, formatado com cores
print('\nSoma total = {}{}{}'.format(cores['azul'], soma, cores['limpa']))


