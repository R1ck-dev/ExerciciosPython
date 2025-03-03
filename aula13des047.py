cores = {'limpa':'\033[m', 'titulo':'\033[1;35m',
         'vermelho':'\033[31m', 'verde':'\033[32m', 'azul':'\033[34m'}

print('-=*=-'*10)
print(' '*18 , '{}EXERCICIO 47{}'.format(cores['titulo'], cores['limpa']))
print('-=*=-'*10)

for c in range (1, 51):
    if c % 2 == 0:
        print('{}{}{} é {}par{}!'.format(cores['titulo'], c, cores['limpa'],
                                         cores['vermelho'], cores['limpa']))
    #else:
        #print('{}{}{} é {}ímpar{}!'.format(cores['titulo'], c, cores['limpa'],
                                         #cores['azul'], cores['limpa']))