import random
from random import randint

cores = {'limpa': '\033[m', 'titulo': '\033[1;35m',
         'vermelho': '\033[31m', 'verde': '\033[32m', 'azul': '\033[34m'}

print('-=*=-' * 10)
print(' ' * 18, f"{cores['titulo']}EXERCICIO 74{cores['limpa']}")
print('-=*=-' * 10)

valores_aleatorios = (randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100))

print(f"{cores['titulo']}Valores sorteados:{cores['limpa']} {cores['azul']}{valores_aleatorios}{cores['limpa']}")
print(f"{cores['vermelho']}Maior valor:{cores['limpa']} {sorted(valores_aleatorios)[-1]}")
print(f"{cores['verde']}Menor valor:{cores['limpa']} {sorted(valores_aleatorios)[0]}")
