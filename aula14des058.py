import random

cores = {'limpa':'\033[m', 'titulo':'\033[1;35m',
         'vermelho':'\033[31m', 'verde':'\033[32m', 'azul':'\033[34m'}

print('-=*=-'*10)
print(' '*18 , '{}EXERCICIO 58{}'.format(cores['titulo'], cores['limpa']))
print('-=*=-'*10)

valor = random.randint(0, 10)
jogada = int(input("Escolha um valor de 0 a 10: "))
tentativas = 1

if jogada != valor:
    while jogada != valor:
        print('Tentativa {}errada!{}'.format(cores['vermelho'], cores['limpa']))
        tentativas += 1
        jogada = int(input("{}[TENTE DE NOVO]{} Escolha um valor de 0 a 10: ".format(cores['titulo'], cores['limpa'])))
    print('Tentativa {}correta!{}'.format(cores['azul'], cores['limpa']))
    print('Foram necessárias {}{}{} tentativas.'.format(cores['verde'], tentativas, cores['limpa']))
else:
    print('Tentativa {}correta!{}'.format(cores['azul'], cores['limpa']))
    print('Foi necessário apenas {}1{} tentativa.'.format(cores['verde'], cores['limpa']))