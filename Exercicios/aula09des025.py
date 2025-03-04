# Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.

# Solicita ao usuário que insira um nome e armazena na variável 'nome'
nome = input('Insira um nome: ')

# Verifica se a string 'Silva' está presente dentro do nome inserido (case-sensitive)
s_n = 'Silva' in nome

# Exibe True se o nome contém 'Silva', caso contrário, exibe False
print(s_n)
