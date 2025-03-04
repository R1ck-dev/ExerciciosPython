# O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

# Importa o módulo random para embaralhar a lista de alunos
import random

# Solicita ao usuário que insira os nomes de quatro alunos
n1 = input('Nome 1: ')
n2 = input('Nome 2: ')
n3 = input('Nome 3: ')
n4 = input('Nome 4: ')

# Cria uma lista contendo os nomes informados
lista_nome = [n1, n2 , n3, n4]

# Utiliza a função shuffle() do módulo random para embaralhar a ordem dos nomes na lista
random.shuffle(lista_nome)

# Exibe a nova ordem sorteada dos alunos
print('A ordem sorteada foi {}.'.format(lista_nome))
