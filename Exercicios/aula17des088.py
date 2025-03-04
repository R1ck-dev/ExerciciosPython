# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

import random  # Módulo para gerar números aleatórios
import time  # Módulo para adicionar pausas na exibição dos resultados

# Dicionário contendo códigos ANSI para colorir a saída no terminal
cores = {'limpa': '\033[m', 'titulo': '\033[1;35m',
         'vermelho': '\033[31m', 'verde': '\033[32m', 'azul': '\033[34m'}

# Impressão do título formatado do exercício
print('-=*=-' * 10)
print(f"{cores['titulo']}EXERCICIO 88{cores['limpa']}".center(60))
print('-=*=-' * 10)

# Solicita ao usuário a quantidade de jogos que deseja sortear
qtd_palpite = int(input("Quantos jogos serão sorteados? "))

# Listas para armazenar os números sorteados
jogada = list()  # Lista temporária para armazenar cada jogo gerado
jogada_final = list()  # Lista composta que armazenará todas as jogadas geradas

# Loop para gerar a quantidade de jogos solicitada
for c in range(0, qtd_palpite):
    for i in range(0, 6):  # Cada jogo contém 6 números aleatórios
        num = random.randint(1, 60)  # Sorteia um número entre 1 e 60
        if num in jogada:  # Garante que não haja números repetidos no jogo
            while num in jogada:  # Repete o sorteio até encontrar um número único
                num = random.randint(1, 60)
        jogada.append(num)  # Adiciona o número à jogada atual
    jogada_final.append(jogada[:])  # Adiciona uma cópia da jogada à lista final
    jogada.clear()  # Limpa a lista temporária para a próxima jogada

# Exibe os jogos gerados
for i, l in enumerate(jogada_final):
    print(f'Jogada[{i+1}] = {sorted(l)}')  # Exibe os números ordenados
    time.sleep(1)  # Adiciona uma pausa de 1 segundo entre as exibições
