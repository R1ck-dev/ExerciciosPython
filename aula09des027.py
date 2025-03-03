nome = input('Insira um nome completo: ')
nome_dividido = nome.split()
print('Primeiro nome: {}'.format(nome_dividido[0][0:]))
print('Último nome: {}'.format(nome_dividido[-1][0:])) # ---> [-1] seleciona o último elemento dessa lista.