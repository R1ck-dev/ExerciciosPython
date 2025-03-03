cores = {'limpa':'\033[m', 'titulo':'\033[1;35m',
         'vermelho':'\033[31m', 'verde':'\033[32m', 'azul':'\033[34m'}

print('-=*=-'*10)
print(' '*18 , '{}EXERCICIO 50{}'.format(cores['titulo'], cores['limpa']))
print('-=*=-'*10)

soma = 0

for c in range(0, 6):
    valor = int(input('Insira um valor qualquer: '))
    if valor % 2 == 0:
        soma += valor
        print('{}{}{} adicionado a soma.'.format(cores['azul'], valor, cores['limpa']))
    else:
        print('{}NÃO{} adicionado a soma.'.format(cores['vermelho'], cores['limpa']))
print('Soma final = {}{}{}'.format(cores['titulo'], soma, cores['limpa']))