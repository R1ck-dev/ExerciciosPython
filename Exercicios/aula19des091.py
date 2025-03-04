# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

import random
import time
from operator import itemgetter

cores = {'limpa': '\033[m', 'titulo': '\033[1;35m',
         'vermelho': '\033[31m', 'verde': '\033[32m', 'azul': '\033[34m'}

print('-=*=-' * 10)
print(f"{cores['titulo']}EXERCICIO 91{cores['limpa']}".center(60))
print('-=*=-' * 10)

jogadas = dict()
jogadas_ordem = dict()

for c in range(0, 4):
    jogadas[f'jogador{c+1}'] = random.randint(1, 6)
for k, v in jogadas.items():
    print(f'O {k} tirou {v} no dado')
    time.sleep(1)
jogadas_ordem = sorted(jogadas.items(), key=itemgetter(1), reverse=True)
print(jogadas_ordem)
for c in range(0, len(jogadas_ordem)):
    print(f'Lugar {c+1}: {jogadas_ordem[c][0]} ({jogadas_ordem[c][1]})')
    time.sleep(1)