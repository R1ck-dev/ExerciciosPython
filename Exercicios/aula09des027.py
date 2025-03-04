# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

# Solicita ao usuário que insira um nome completo e armazena na variável 'nome'
nome = input('Insira um nome completo: ')

# Divide o nome completo em uma lista de palavras (separadas pelos espaços)
nome_dividido = nome.split()

# Exibe o primeiro nome, que está na posição 0 da lista
print('Primeiro nome: {}'.format(nome_dividido[0][0:]))

# Exibe o último nome, que está na última posição da lista (índice -1)
print('Último nome: {}'.format(nome_dividido[-1][0:]))  # [-1] seleciona o último elemento da lista.
