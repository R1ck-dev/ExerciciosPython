cores = {'limpa':'\033[m', 'titulo':'\033[1;35m',
         'vermelho':'\033[31m', 'verde':'\033[32m', 'azul':'\033[34m'}

print('-=*=-'*10)
print(' '*18 , '{}EXERCICIO 37{}'.format(cores['titulo'], cores['limpa']))
print('-=*=-'*10)

decimal = int(input('Insira o valor decimal: '))

print('\n{}Indique a conversão:{}'.format(cores['azul'], cores['limpa']))
print('{}1 --> Binário{}'.format(cores['verde'], cores['limpa']))
print('{}2 --> Octal{}'.format(cores['verde'], cores['limpa']))
print('{}3 --> Hexadecimal{}'.format(cores['verde'], cores['limpa']))

s_n = int(input('\nIndique: '))

if s_n == 1:
    print('\n{} convertido para binário --> {}{}{}'.format(decimal, cores['azul'], bin(decimal)[2:], cores['limpa']))
elif s_n == 2:
    print('\n{} convertido para octal --> {}{}{}'.format(decimal, cores['azul'], oct(decimal)[2:], cores['limpa']))
elif s_n == 3:
    print('\n{} convertido para hexadecimal --> {}{}{}'.format(decimal, cores['azul'], hex(decimal)[2:], cores['limpa']))
