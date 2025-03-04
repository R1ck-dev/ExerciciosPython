# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.

# Importa a função sleep da biblioteca time para criar pausas na contagem
from time import sleep

# Dicionário contendo códigos ANSI para formatação de cores no terminal
cores = {'limpa':'\033[m', 'titulo':'\033[1;35m',
         'vermelho':'\033[31m', 'verde':'\033[32m', 'azul':'\033[34m'}

# Exibição do cabeçalho formatado no terminal
print('-=*=-'*10)
print(' '*18 , '{}EXERCICIO 46{}'.format(cores['titulo'], cores['limpa']))
print('-=*=-'*10)

# Loop de contagem regressiva de 10 até 0 (incluindo o 0)
for c in range(10, -1, -1):  # O terceiro argumento "-1" faz a contagem decrescer
    print(c)  # Exibe o número atual da contagem
    sleep(1)  # Aguarda 1 segundo antes de continuar para o próximo número

# Exibe a mensagem de estouro dos fogos após a contagem regressiva
print('{}FOGOS!{}'.format(cores['vermelho'], cores['limpa']))
