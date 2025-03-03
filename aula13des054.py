import datetime

cores = {'limpa':'\033[m', 'titulo':'\033[1;35m',
         'vermelho':'\033[31m', 'verde':'\033[32m', 'azul':'\033[34m'}

print('-=*=-'*10)
print(' '*18 , '{}EXERCICIO 54{}'.format(cores['titulo'], cores['limpa']))
print('-=*=-'*10)

data_atual = datetime.datetime.now()
data = data_atual.date()
ano_atual = data.year
soma_menores = 0
soma_maiores = 0

for c in range(0, 7):
    nascimento = int(input('Insira o seu ano de nascimento: '))
    idade = ano_atual - nascimento
    print('{}{}{} ano(s)'.format(cores['titulo'], idade, cores['limpa']))
    if idade < 18:
        print('+ 1 {}menor de idade{}'.format(cores['vermelho'], cores['limpa']))
        soma_menores += 1
    else:
        print('+ 1 {}maior de idade{}'.format(cores['azul'], cores['limpa']))
        soma_maiores += 1

print('\n{}Maiores de idade{} = {}'.format(cores['azul'], cores['limpa'], soma_maiores))
print('{}Menores de idade{} = {}'.format(cores['vermelho'], cores['limpa'], soma_menores))