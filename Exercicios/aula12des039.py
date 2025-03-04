# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

# Importa a biblioteca datetime para obter o ano atual
import datetime

# Dicionário contendo códigos ANSI para formatação de cores no terminal
cores = {'limpa':'\033[m', 'titulo':'\033[1;35m',
         'vermelho':'\033[31m', 'verde':'\033[32m', 'azul':'\033[34m'}

# Exibição do cabeçalho formatado no terminal
print('-=*=-'*10)
print(' '*18 , '{}EXERCICIO 39{}'.format(cores['titulo'], cores['limpa']))
print('-=*=-'*10)

# Solicita ao usuário que insira seu ano de nascimento
nascimento = int(input('Insira o seu ano de nascimento: '))

# Pergunta se o usuário já realizou o alistamento e armazena a resposta
s_n = input('Você já realizou o seu alistamento? [s] ou [n]: ')

# Obtém a data e o ano atual do sistema
data_atual = datetime.datetime.now()
data = data_atual.date()
ano_atual = data.year

# Calcula a idade do usuário com base no ano atual e no ano de nascimento informado
idade = ano_atual - nascimento

# Verifica se o usuário já realizou o alistamento
if s_n == 's':
    # Se a resposta for 's', significa que o alistamento já foi feito
    print('Seu alistamento já foi realizado!')

elif s_n == 'n':
    # Se a resposta for 'n', verifica a idade do usuário para determinar a situação do alistamento
    if idade < 18:
        # Caso o usuário tenha menos de 18 anos, informa quantos anos faltam para o alistamento
        print('Alistamento {}ainda necessário{} em {}{}{} ano(s)'.format(cores['azul'], cores['limpa'],
                                                                       cores['titulo'], (18-idade), cores['limpa']))
    elif idade == 18:
        # Caso o usuário tenha exatamente 18 anos, informa que é o momento de se alistar
        print('É o momento de se alistar!')

    else:
        # Caso o usuário tenha mais de 18 anos, informa quantos anos já passaram do prazo de alistamento
        print('O período de se alistar {}já se excedeu{} em {}{}{} ano(s)'.format(cores['vermelho'], cores['limpa'],
                                                                       cores['titulo'], (idade-18), cores['limpa']))
