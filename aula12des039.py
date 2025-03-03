import datetime

cores = {'limpa':'\033[m', 'titulo':'\033[1;35m',
         'vermelho':'\033[31m', 'verde':'\033[32m', 'azul':'\033[34m'}

print('-=*=-'*10)
print(' '*18 , '{}EXERCICIO 39{}'.format(cores['titulo'], cores['limpa']))
print('-=*=-'*10)

nascimento = int(input('Insira o seu ano de nascimento: '))
s_n = input('Você já realizou o seu alistamento? [s] ou [n]: ')
data_atual = datetime.datetime.now()
data = data_atual.date()
ano_atual = data.year
idade = ano_atual-nascimento

if s_n == 's':
    print('Seu alistamento já foi realizado!')
elif s_n == 'n':
    if idade < 18:
        print('Alistamento {}ainda necessário{} em {}{}{} ano(s)'.format(cores['azul'], cores['limpa'],
                                                                       cores['titulo'], (18-idade), cores['limpa']))
    elif idade == 18:
        print('É o momento de se alistar!')
    else:
        print('O período de se alistar {}já se excedeu{} em {}{}{} ano(s)'.format(cores['vermelho'], cores['limpa'],
                                                                       cores['titulo'], (idade-18), cores['limpa']))