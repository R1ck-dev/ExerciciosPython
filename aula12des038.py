cores = {'limpa':'\033[m', 'titulo':'\033[1;35m',
         'vermelho':'\033[31m', 'verde':'\033[32m', 'azul':'\033[34m'}

print('-=*=-'*10)
print(' '*18 , '{}EXERCICIO 38{}'.format(cores['titulo'], cores['limpa']))
print('-=*=-'*10)

valor1 = int(input('Insira um valor qualquer: '))
valor2 = int(input('Insira um valor qualquer: '))

if valor1 > valor2:
    print('{}{}{} é maior que {}{}{}'.format(cores['verde'], valor1, cores['limpa'],
                                             cores['vermelho'], valor2, cores['limpa']))
elif valor2 > valor1:
    print('{}{}{} é maior que {}{}{}'.format(cores['verde'], valor2, cores['limpa'],
                                             cores['vermelho'], valor1, cores['limpa']))
else:
    print('Não existe valor maior, os dois são iguais!')