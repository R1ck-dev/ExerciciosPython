# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

# Importação do módulo random e da função randint para gerar números aleatórios
import random
from random import randint

# Dicionário contendo códigos ANSI para colorir a saída no terminal
cores = {'limpa': '\033[m', 'titulo': '\033[1;35m',
         'vermelho': '\033[31m', 'verde': '\033[32m', 'azul': '\033[34m'}

# Impressão do título formatado do exercício
print('-=*=-' * 10)
print(' ' * 18, f"{cores['titulo']}EXERCICIO 74{cores['limpa']}")
print('-=*=-' * 10)

# Criação de uma tupla com 5 números aleatórios entre 1 e 100
valores_aleatorios = (randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100))

# Exibição da tupla com os números sorteados
print(f"{cores['titulo']}Valores sorteados:{cores['limpa']} {cores['azul']}{valores_aleatorios}{cores['limpa']}")

# Exibição do maior valor da tupla
print(f"{cores['vermelho']}Maior valor:{cores['limpa']} {sorted(valores_aleatorios)[-1]}")

# Exibição do menor valor da tupla
print(f"{cores['verde']}Menor valor:{cores['limpa']} {sorted(valores_aleatorios)[0]}")

