cores = {'limpa':'\033[m', 'titulo':'\033[1;35m',
         'vermelho':'\033[31m', 'verde':'\033[32m', 'azul':'\033[34m'}

print('-=*=-'*10)
print(' '*18 , '{}EXERCICIO 63{}'.format(cores['titulo'], cores['limpa']))
print('-=*=-'*10)

valor = int(input('Insira um valor qualquer: '))
cont = soma = 0

while valor != 999:
    cont += 1
    soma += valor
    valor = int(input('Insira um valor qualquer: ')) #para nn contar o 999, deixar no final
print('Soma = {}\nContador = {}'.format(soma, cont))