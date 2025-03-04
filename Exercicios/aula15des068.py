# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

import random

# Dicionário de cores para formatação no terminal
cores = {'limpa': '\033[m', 'titulo': '\033[1;35m',
         'vermelho': '\033[31m', 'verde': '\033[32m', 'azul': '\033[34m'}

# Exibição do título formatado
print('-=*=-' * 10)
print(' ' * 18, '{}EXERCICIO 68{}'.format(cores['titulo'], cores['limpa']))
print('-=*=-' * 10)

# Inicializa a contagem de vitórias consecutivas
vitorias = 0

# Loop principal do jogo
while True:
    # Jogador escolhe entre "par" ou "ímpar"
    escolha_jogador = input('Escolha par ou impar: ').lower()

    # Se o jogador escolheu ÍMPAR
    if escolha_jogador == 'impar':
        jogada_jogador = int(input('Faça a sua jogada: '))  # Jogador insere um número
        jogada_pc = random.randint(0, 2 ** 53)  # Computador escolhe um número aleatório
        par_impar = (jogada_jogador + jogada_pc) % 2  # Verifica se a soma é PAR ou ÍMPAR

        # Verifica se o jogador venceu
        if par_impar != 0:  # Se a soma for ÍMPAR, jogador vence
            print('{}Jogador Venceu!{}'.format(cores['verde'], cores['limpa']))
            vitorias += 1  # Incrementa a contagem de vitórias
            print('{}-=*=-{}'.format(cores['titulo'], cores['limpa']) * 10)
            print(f'Você jogou {jogada_jogador}, e o computador jogou {jogada_pc}')
            print(f'Total deu {jogada_jogador + jogada_pc}, portanto ÍMPAR')
            print('{}-=*=-{}'.format(cores['titulo'], cores['limpa']) * 10)
        else:  # Se a soma for PAR, computador vence e o jogo termina
            print('{}Máquina Venceu!{}'.format(cores['vermelho'], cores['limpa']))
            print('{}-=*=-{}'.format(cores['titulo'], cores['limpa']) * 10)
            print(f'Você jogou {jogada_jogador}, e o computador jogou {jogada_pc}')
            print(f'Total deu {jogada_jogador + jogada_pc}, portanto PAR')
            print('{}-=*=-{}'.format(cores['titulo'], cores['limpa']) * 10)
            break

    # Se o jogador escolheu PAR
    elif escolha_jogador == 'par':
        jogada_jogador = int(input('Faça a sua jogada: '))
        jogada_pc = random.randint(0, 10)  # Computador escolhe um número aleatório entre 0 e 10
        par_impar = (jogada_jogador + jogada_pc) % 2  # Verifica se a soma é PAR ou ÍMPAR

        # Verifica se o jogador venceu
        if par_impar == 0:  # Se a soma for PAR, jogador vence
            print('{}Jogador Venceu!{}'.format(cores['verde'], cores['limpa']))
            vitorias += 1  # Incrementa a contagem de vitórias
            print('{}-=*=-{}'.format(cores['titulo'], cores['limpa']) * 10)
            print(f'Você jogou {jogada_jogador}, e o computador jogou {jogada_pc}')
            print(f'Total deu {jogada_jogador + jogada_pc}, portanto PAR')
            print('{}-=*=-{}'.format(cores['titulo'], cores['limpa']) * 10)
        else:  # Se a soma for ÍMPAR, computador vence e o jogo termina
            print('{}Máquina Venceu!{}'.format(cores['vermelho'], cores['limpa']))
            print('{}-=*=-{}'.format(cores['titulo'], cores['limpa']) * 10)
            print(f'Você jogou {jogada_jogador}, e o computador jogou {jogada_pc}')
            print(f'Total deu {jogada_jogador + jogada_pc}, portanto ÍMPAR')
            print('{}-=*=-{}'.format(cores['titulo'], cores['limpa']) * 10)
            break

    # Caso o jogador digite algo inválido
    else:
        print('Escolha Inválida')

# Exibição do resultado final
print('{}Game Over!{}'.format(cores['vermelho'], cores['limpa']))
print('Total de vitórias consecutivas: {}{}{}'.format(cores['verde'], vitorias, cores['limpa']))
