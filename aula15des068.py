import random

cores = {'limpa':'\033[m', 'titulo':'\033[1;35m',
         'vermelho':'\033[31m', 'verde':'\033[32m', 'azul':'\033[34m'}

print('-=*=-'*10)
print(' '*18 , '{}EXERCICIO 68{}'.format(cores['titulo'], cores['limpa']))
print('-=*=-'*10)

vitorias = 0

while True:
    escolha_jogador = input('Escolha par ou impar: ').lower()
    if escolha_jogador == 'impar':

        jogada_jogador = int(input('Faça a sua jogada: '))
        jogada_pc = random.randint(0, 2 ** 53)
        par_impar = (jogada_jogador + jogada_pc) % 2

        if par_impar != 0:
            print('{}Jogador Venceu!{}'.format(cores['verde'], cores['limpa']))
            vitorias += 1
            print('{}-=*=-{}'.format(cores['titulo'], cores['limpa']) * 10)
            print(f'Você jogou {jogada_jogador}, e o computador jogou {jogada_pc}')
            print(f'Total deu {jogada_jogador+jogada_pc}, portanto ÍMPAR')
            print('{}-=*=-{}'.format(cores['titulo'], cores['limpa']) * 10)
        else:
            print('{}Máquina Venceu!{}'.format(cores['vermelho'], cores['limpa']))
            print('{}-=*=-{}'.format(cores['titulo'], cores['limpa']) * 10)
            print(f'Você jogou {jogada_jogador}, e o computador jogou {jogada_pc}')
            print(f'Total deu {jogada_jogador + jogada_pc}, portanto PAR')
            print('{}-=*=-{}'.format(cores['titulo'], cores['limpa']) * 10)
            break

    elif escolha_jogador == 'par':

        jogada_jogador = int(input('Faça a sua jogada: '))
        jogada_pc = random.randint(0, 10)
        par_impar = (jogada_jogador + jogada_pc) % 2

        if par_impar == 0:
            print('{}Jogador Venceu!{}'.format(cores['verde'], cores['limpa']))
            vitorias += 1
            print('{}-=*=-{}'.format(cores['titulo'], cores['limpa']) * 10)
            print(f'Você jogou {jogada_jogador}, e o computador jogou {jogada_pc}')
            print(f'Total deu {jogada_jogador + jogada_pc}, portanto PAR')
            print('{}-=*=-{}'.format(cores['titulo'], cores['limpa']) * 10)
        else:
            print('{}Máquina Venceu!{}'.format(cores['vermelho'], cores['limpa']))
            print('{}-=*=-{}'.format(cores['titulo'], cores['limpa']) * 10)
            print(f'Você jogou {jogada_jogador}, e o computador jogou {jogada_pc}')
            print(f'Total deu {jogada_jogador + jogada_pc}, portanto ÍMPAR')
            print('{}-=*=-{}'.format(cores['titulo'], cores['limpa']) * 10)
            break

    else:
        print('Escolha Inválida')

print('{}Game Over!{}'.format(cores['vermelho'], cores['limpa']))
print('Total de vitórias consecutivas: {}{}{}'.format(cores['verde'], vitorias, cores['limpa']))

