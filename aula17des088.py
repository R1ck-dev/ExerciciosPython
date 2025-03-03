import random
import time

cores = {'limpa': '\033[m', 'titulo': '\033[1;35m',
         'vermelho': '\033[31m', 'verde': '\033[32m', 'azul': '\033[34m'}

print('-=*=-' * 10)
print(f"{cores['titulo']}EXERCICIO 88{cores['limpa']}".center(60))
print('-=*=-' * 10)

qtd_palpite = int(input("Quantos jogos serão sorteados? "))
jogada = list()
jogada_final = list() 

for c in range(0, qtd_palpite):
    for i in range(0, 6):
        num = random.randint(1, 60)
        if num in jogada:
            while num in jogada:
                num = random.randint(1, 60)
        jogada.append(num)
    jogada_final.append(jogada[:])
    jogada.clear()
for i, l in enumerate(jogada_final):
    print(f'Jogada[{i+1}] = {sorted(l)}')
    time.sleep(1)