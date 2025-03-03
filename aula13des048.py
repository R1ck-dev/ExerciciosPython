cores = {'limpa':'\033[m', 'titulo':'\033[1;35m',
         'vermelho':'\033[31m', 'verde':'\033[32m', 'azul':'\033[34m'}

print('-=*=-'*10)
print(' '*18 , '{}EXERCICIO 48{}'.format(cores['titulo'], cores['limpa']))
print('-=*=-'*10)

soma = 0

for c in range (1, 501):
    if c % 2 != 0:
        if c % 3 == 0:
            print('{}{}{} é ímpar e múltiplo de 3'.format(cores['vermelho'], c, cores['limpa']))
            soma += c

print('\nSoma total = {}{}{}'.format(cores['azul'], soma, cores['limpa']))

