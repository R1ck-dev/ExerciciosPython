cores = {'limpa':'\033[m', 'titulo':'\033[1;35m',
         'vermelho':'\033[31m', 'verde':'\033[32m', 'azul':'\033[34m'}

print('-=*=-'*10)
print(' '*18 , '{}EXERCICIO 60{}'.format(cores['titulo'], cores['limpa']))
print('-=*=-'*10)

multiplicador = valor = int(input('Insira o valor: '))
valor_novo = 1

while multiplicador > 1:
    valor_novo *= multiplicador
    multiplicador -= 1

print('{}{}!{} = {}{}{}'.format(cores['vermelho'], valor, cores['limpa'],
                                cores['azul'], valor_novo, cores['limpa']))