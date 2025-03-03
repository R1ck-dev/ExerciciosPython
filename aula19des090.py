cores = {'limpa': '\033[m', 'titulo': '\033[1;35m',
         'vermelho': '\033[31m', 'verde': '\033[32m', 'azul': '\033[34m'}

print('-=*=-' * 10)
print(f"{cores['titulo']}EXERCICIO 90{cores['limpa']}".center(60))
print('-=*=-' * 10)

aluno = dict()

aluno['nome'] = str(input("Nome: "))
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['media'] >= 6:
    aluno['sitaucao'] = 'aprovado'
else:
    aluno['sitaucao'] = 'reprovado'
print(f'Nome é igual a {aluno["nome"]}')
print(f'Média é igual a {aluno["media"]}')
print(f'Situação é igual a {aluno["sitaucao"]}')


