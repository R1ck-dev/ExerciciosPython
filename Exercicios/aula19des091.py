# Importa os módulos necessários
import random
import time
from operator import itemgetter

# Dicionário com códigos ANSI para colorir a saída no terminal
cores = {'limpa': '\033[m', 'titulo': '\033[1;35m',
         'vermelho': '\033[31m', 'verde': '\033[32m', 'azul': '\033[34m'}

# Impressão do título formatado do exercício
print('-=*=-' * 10)
print(f"{cores['titulo']}EXERCICIO 91{cores['limpa']}".center(60))
print('-=*=-' * 10)

# Dicionário para armazenar as jogadas dos jogadores
jogadas = dict()
jogadas_ordem = dict()

# Simula o lançamento de dados para 4 jogadores
for c in range(0, 4):  # Repete para 4 jogadores
    jogadas[f'jogador{c+1}'] = random.randint(1, 6)  # Sorteia um número de 1 a 6 para cada jogador

# Exibe o resultado de cada jogador
for k, v in jogadas.items():
    print(f'O {k} tirou {v} no dado')  # Mostra o nome do jogador e o número tirado
    time.sleep(1)  # Pausa de 1 segundo entre os resultados

# Organiza as jogadas em ordem decrescente de acordo com o número sorteado
jogadas_ordem = sorted(jogadas.items(), key=itemgetter(1), reverse=True)

# Exibe a lista ordenada de jogadores e suas jogadas
print(jogadas_ordem)  # Exibe a lista de jogadas ordenadas
for c in range(0, len(jogadas_ordem)):  # Percorre a lista ordenada
    print(f'Lugar {c+1}: {jogadas_ordem[c][0]} ({jogadas_ordem[c][1]})')  # Exibe o ranking dos jogadores
    time.sleep(1)  # Pausa de 1 segundo entre os resultados
