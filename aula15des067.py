cores = {'limpa':'\033[m', 'titulo':'\033[1;35m',
         'vermelho':'\033[31m', 'verde':'\033[32m', 'azul':'\033[34m'}

print('-=*=-'*10)
print(' '*18 , '{}EXERCICIO 67{}'.format(cores['titulo'], cores['limpa']))
print('-=*=-'*10)


while True:
    valor = int(input('Deseja ver a tabuada de qual número: '))
    if valor < 0:
        break
    multiplicador = 1
    print('{}-=*=-{}'.format(cores['verde'], cores['limpa']) * 10)
    while multiplicador <= 10:
        print('{}{}{} x {} = {}{}{}'.format(cores['vermelho'], multiplicador, cores['limpa'],
                                            valor, cores['titulo'], valor*multiplicador, cores['limpa']))
        multiplicador += 1
    print('{}-=*=-{}'.format(cores['verde'], cores['limpa']) * 10)
print('{}---FINALIZADO---{}'.format(cores['vermelho'], cores['limpa']))
