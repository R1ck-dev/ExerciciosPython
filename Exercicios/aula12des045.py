# Crie um programa que faça o computador jogar Jokenpô com você.

# Dicionário contendo códigos ANSI para formatação de cores no terminal
cores = {'limpa':'\033[m', 'titulo':'\033[1;35m',
         'vermelho':'\033[31m', 'verde':'\033[32m', 'azul':'\033[34m'}

# Exibição do cabeçalho formatado no terminal
print('-=*=-'*10)
print(' '*18 , '{}EXERCICIO 45{}'.format(cores['titulo'], cores['limpa']))
print('-=*=-'*10)

# Exibição das opções para o jogador escolher
print('\n{}Indique a sua jogada:{}'.format(cores['azul'], cores['limpa']))
print('{}1 --> Pedra{}'.format(cores['verde'], cores['limpa']))
print('{}2 --> Papel{}'.format(cores['verde'], cores['limpa']))
print('{}3 --> Tesoura{}'.format(cores['verde'], cores['limpa']))

# Captura a jogada de ambos os jogadores
jogador1 = int(input('\n{}[JOGADOR 1]{} Jogue: '.format(cores['vermelho'], cores['limpa'])))
jogador2 = int(input('{}[JOGADOR 2]{} Jogue: '.format(cores['vermelho'], cores['limpa'])))

# Verifica a jogada do Jogador 1 e compara com a jogada do Jogador 2
if jogador1 == 1:  # Jogador 1 escolheu Pedra
    if jogador2 == 1:
        print('\nPedra x Pedra')
        print('{}EMPATE!{}'.format(cores['azul'], cores['limpa']))
    elif jogador2 == 2:
        print('\nPedra x Papel')
        print('Jogador 2 {}VENCE!{}'.format(cores['verde'], cores['limpa']))
    elif jogador2 == 3:
        print('\nPedra x Tesoura')
        print('Jogador 1 {}VENCE!{}'.format(cores['verde'], cores['limpa']))

elif jogador1 == 2:  # Jogador 1 escolheu Papel
    if jogador2 == 1:
        print('\nPapel x Pedra')
        print('Jogador 1 {}VENCE!{}'.format(cores['verde'], cores['limpa']))
    elif jogador2 == 2:
        print('\nPapel x Papel')
        print('{}EMPATE!{}'.format(cores['azul'], cores['limpa']))
    elif jogador2 == 3:
        print('\nPapel x Tesoura')
        print('Jogador 2 {}VENCE!{}'.format(cores['verde'], cores['limpa']))

elif jogador1 == 3:  # Jogador 1 escolheu Tesoura
    if jogador2 == 1:
        print('\nTesoura x Pedra')
        print('Jogador 2 {}VENCE!{}'.format(cores['verde'], cores['limpa']))
    elif jogador2 == 2:
        print('\nTesoura x Papel')
        print('Jogador 1 {}VENCE!{}'.format(cores['verde'], cores['limpa']))
    elif jogador2 == 3:
        print('\nTesoura x Tesoura')
        print('{}EMPATE!{}'.format(cores['azul'], cores['limpa']))
