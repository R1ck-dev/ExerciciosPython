# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

# Importa o módulo random para realizar a escolha aleatória de um item da lista
import random

# Solicita ao usuário que insira os nomes de quatro alunos
n1 = input('Nome 1: ')
n2 = input('Nome 2: ')
n3 = input('Nome 3: ')
n4 = input('Nome 4: ')

# Cria uma lista contendo os nomes informados
lista_nome = [n1, n2 , n3, n4]

# Utiliza a função choice() do módulo random para escolher aleatoriamente um nome da lista
escolhido = random.choice(lista_nome)

# Exibe o nome do aluno escolhido
print('O aluno sorteado foi {}.'.format(escolhido))
