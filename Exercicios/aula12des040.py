# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
#
# – Média abaixo de 5.0: REPROVADO
#
# – Média entre 5.0 e 6.9: RECUPERAÇÃO
#
# – Média 7.0 ou superior: APROVADO

# Dicionário contendo códigos ANSI para formatação de cores no terminal
cores = {'limpa':'\033[m', 'titulo':'\033[1;35m',
         'vermelho':'\033[31m', 'verde':'\033[32m', 'azul':'\033[34m'}

# Exibição do cabeçalho formatado no terminal
print('-=*=-'*10)
print(' '*18 , '{}EXERCICIO 40{}'.format(cores['titulo'], cores['limpa']))
print('-=*=-'*10)

# Solicita ao usuário que insira duas notas
nota1 = float(input('Insira a nota 1: '))
nota2 = float(input('Insira a nota 2: '))

# Calcula a média das notas inseridas
media = (nota1 + nota2) / 2

# Verifica a situação do aluno com base na média obtida
if media < 5:
    # Caso a média seja inferior a 5, o aluno está reprovado
    print('Média: {:.2f}'.format(media))
    print('{}REPROVADO!{}'.format(cores['vermelho'], cores['limpa']))

elif media >= 5 and media < 7:
    # Caso a média esteja entre 5 e 6.9, o aluno está de recuperação
    print('Média: {:.2f}'.format(media))
    print('{}RECUPERAÇÃO!{}'.format(cores['azul'], cores['limpa']))

elif media >= 7:
    # Caso a média seja 7 ou superior, o aluno está aprovado
    print('Média: {:.2f}'.format(media))
    print('{}APROVADO!{}'.format(cores['verde'], cores['limpa']))
