cores = {'limpa':'\033[m', 'titulo':'\033[1;35m',
         'vermelho':'\033[31m', 'verde':'\033[32m', 'azul':'\033[34m'}

print('-=*=-'*10)
print(' '*18 , '{}EXERCICIO 45{}'.format(cores['titulo'], cores['limpa']))
print('-=*=-'*10)

print('\n{}Indique a sua jogada:{}'.format(cores['azul'], cores['limpa']))
print('{}1 --> Pedra{}'.format(cores['verde'], cores['limpa']))
print('{}2 --> Papel{}'.format(cores['verde'], cores['limpa']))
print('{}3 --> Tesoura{}'.format(cores['verde'], cores['limpa']))

jogador1 = int(input('\n{}[JOGADOR 1]{} Jogue: '.format(cores['vermelho'], cores['limpa'])))
jogador2 = int(input('{}[JOGADOR 2]{} Jogue: '.format(cores['vermelho'], cores['limpa'])))

if jogador1 == 1:
    if jogador2 == 1:
        print('\nPedra x Pedra')
        print('{}EMPATE!{}'.format(cores['azul'], cores['limpa']))
    elif jogador2 == 2:
        print('\nPedra x Papel')
        print('Jogador 2 {}VENCE!{}'.format(cores['verde'], cores['limpa']))
    elif jogador2 == 3:
        print('\nPedra x Tesoura')
        print('Jogador 1 {}VENCE!{}'.format(cores['verde'], cores['limpa']))
elif jogador1 == 2:
    if jogador2 == 1:
        print('\nPapel x Pedra')
        print('Jogador 1 {}VENCE!{}'.format(cores['verde'], cores['limpa']))
    elif jogador2 == 2:
        print('\nPapel x Papel')
        print('{}EMPATE!{}'.format(cores['azul'], cores['limpa']))
    elif jogador2 == 3:
        print('\nPapel x Tesoura')
        print('Jogador 2 {}VENCE!{}'.format(cores['verde'], cores['limpa']))
elif jogador1 == 3:
    if jogador2 == 1:
        print('\nTesoura x Pedra')
        print('\nJogador 2 {}VENCE!{}'.format(cores['verde'], cores['limpa']))
    elif jogador2 == 2:
        print('\nTesoura x Papel')
        print('\nJogador 1 {}VENCE!{}'.format(cores['verde'], cores['limpa']))
    elif jogador2 == 3:
        print('\nTesoura x Tesoura')
        print('{}EMPATE!{}'.format(cores['azul'], cores['limpa']))