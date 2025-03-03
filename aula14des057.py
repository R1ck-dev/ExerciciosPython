cores = {'limpa':'\033[m', 'titulo':'\033[1;35m',
         'vermelho':'\033[31m', 'verde':'\033[32m', 'azul':'\033[34m'}

print('-=*=-'*10)
print(' '*18 , '{}EXERCICIO 57{}'.format(cores['titulo'], cores['limpa']))
print('-=*=-'*10)

sexo = ''

while sexo != 'F' and sexo != 'M':
    sexo = input('Insira o sexo [F/M]: ').upper()
    print('Sexo informado {}[{}]{}.'.format(cores['titulo'], sexo, cores['limpa']))
print('{}---FINALIZADO---{}'.format(cores['vermelho'], cores['limpa']))
