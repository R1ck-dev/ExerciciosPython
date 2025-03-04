# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.

# Dicionário contendo códigos ANSI para colorir a saída no terminal
cores = {'limpa': '\033[m', 'titulo': '\033[1;35m',
         'vermelho': '\033[31m', 'verde': '\033[32m', 'azul': '\033[34m'}

# Impressão do título formatado do exercício
print('-=*=-' * 10)
print(f"{cores['titulo']}EXERCICIO 90{cores['limpa']}".center(60))
print('-=*=-' * 10)

# Criação de um dicionário para armazenar os dados do aluno
aluno = dict()

# Leitura do nome e da média do aluno
aluno['nome'] = str(input("Nome: "))  # Armazena o nome no dicionário
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))  # Armazena a média

# Determinação da situação do aluno com base na média
if aluno['media'] >= 6:
    aluno['sitaucao'] = 'aprovado'  # Aluno aprovado se a média for 6 ou mais
else:
    aluno['sitaucao'] = 'reprovado'  # Aluno reprovado se a média for menor que 6

# Exibição das informações armazenadas no dicionário
print(f'Nome é igual a {aluno["nome"]}')
print(f'Média é igual a {aluno["media"]}')
print(f'Situação é igual a {aluno["sitaucao"]}')



