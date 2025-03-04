# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome Santo

# Solicita ao usuário que insira o nome de uma cidade e armazena na variável 'nome'
nome = str(input('Insira o nome de uma cidade: '))

# Divide o nome da cidade em uma lista de palavras, separando pelos espaços
primeira_palavra = nome.split()

# Verifica se a primeira palavra da lista contém a palavra 'Santo'
s_n = 'Santo' in primeira_palavra[0][0:]

# Exibe o resultado da verificação, retornando True se começar com "Santo" e False caso contrário
print(s_n)
