# Crie um programa que leia o nome completo de uma pessoa e mostre:
#
# – O nome com todas as letras maiúsculas e minúsculas.
#
# – Quantas letras ao todo (sem considerar espaços).
#
# – Quantas letras tem o primeiro nome.

# Solicita ao usuário que insira um nome completo
nome = str(input('Insira um nome completo: '))

# Exibe o nome todo em letras maiúsculas
print('Nome completo maiúsculo: {}'.format(nome.upper()))

# Exibe o nome todo em letras minúsculas
print('Nome completo minúsculo: {}'.format(nome.lower()))

# Conta a quantidade de letras no nome, desconsiderando os espaços
print('Quantidade de letras (sem considerar espaços): {}'.format(len(nome.replace(' ', ''))))

# Divide o nome em partes, separando pelo espaço
nome_dividido = nome.split()

# Exibe a quantidade de letras do primeiro nome
print('Letras no primeiro nome: {}'.format(len(nome_dividido[0][0:])))


