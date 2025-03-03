from time import sleep

cores = {'limpa':'\033[m', 'titulo':'\033[1;35m',
         'vermelho':'\033[31m', 'verde':'\033[32m', 'azul':'\033[34m'}

print('-=*=-'*10)
print(' '*18 , '{}EXERCICIO 46{}'.format(cores['titulo'], cores['limpa']))
print('-=*=-'*10)

for c in range (10, -1, -1):
    print(c)
    sleep(1)
print('{}FOGOS!{}'.format(cores['vermelho'], cores['limpa']))