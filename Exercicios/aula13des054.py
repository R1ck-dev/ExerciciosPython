# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

import datetime  # Importa o módulo datetime para obter o ano atual

# Dicionário contendo códigos ANSI para formatação de cores no terminal
cores = {'limpa':'\033[m', 'titulo':'\033[1;35m',
         'vermelho':'\033[31m', 'verde':'\033[32m', 'azul':'\033[34m'}

# Exibição do cabeçalho do exercício formatado com cores
print('-=*=-'*10)
print(' '*18 , '{}EXERCICIO 54{}'.format(cores['titulo'], cores['limpa']))
print('-=*=-'*10)

# Obtém o ano atual usando datetime
data_atual = datetime.datetime.now()
data = data_atual.date()
ano_atual = data.year  # Extração apenas do ano

# Inicializa contadores para armazenar o número de menores e maiores de idade
soma_menores = 0
soma_maiores = 0

# Loop para ler o ano de nascimento de 7 pessoas
for c in range(0, 7):
    nascimento = int(input('Insira o seu ano de nascimento: '))  # Entrada do ano de nascimento
    idade = ano_atual - nascimento  # Cálculo da idade
    print('{}{}{} ano(s)'.format(cores['titulo'], idade, cores['limpa']))  # Exibe a idade calculada

    # Verifica se a pessoa é menor ou maior de idade
    if idade < 18:
        print('+ 1 {}menor de idade{}'.format(cores['vermelho'], cores['limpa']))
        soma_menores += 1  # Incrementa o contador de menores de idade
    else:
        print('+ 1 {}maior de idade{}'.format(cores['azul'], cores['limpa']))
        soma_maiores += 1  # Incrementa o contador de maiores de idade

# Exibição do resultado final
print('\n{}Maiores de idade{} = {}'.format(cores['azul'], cores['limpa'], soma_maiores))
print('{}Menores de idade{} = {}'.format(cores['vermelho'], cores['limpa'], soma_menores))
