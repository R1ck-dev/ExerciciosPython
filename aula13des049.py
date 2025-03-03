cores = {'limpa':'\033[m', 'titulo':'\033[1;35m',
         'vermelho':'\033[31m', 'verde':'\033[32m', 'azul':'\033[34m'}

print('-=*=-'*10)
print(' '*18 , '{}EXERCICIO 49{}'.format(cores['titulo'], cores['limpa']))
print('-=*=-'*10)

tab = int(input('Indique qual tabuada deseja acessar: '))

for c in range (0, 11):
    print('{}{}{} x {} = {}{}{}'.format(cores['vermelho'], tab, cores['limpa'],
                                            c, cores['titulo'], tab*c, cores['limpa']))