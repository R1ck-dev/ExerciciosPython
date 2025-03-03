import random
n1 = input('Nome 1: ')
n2 = input('Nome 2: ')
n3 = input('Nome 3: ')
n4 = input('Nome 4: ')
lista_nome = [n1, n2 , n3, n4]
escolhido = random.choice(lista_nome)
print('O aluno sorteado foi {}.'.format(escolhido))