# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
#
# – Até 9 anos: MIRIM
#
# – Até 14 anos: INFANTIL
#
# – Até 19 anos: JÚNIOR
#
# – Até 25 anos: SÊNIOR
#
# – Acima de 25 anos: MASTER

# Importa a biblioteca datetime para obter o ano atual
import datetime

# Dicionário contendo códigos ANSI para formatação de cores no terminal
cores = {'limpa':'\033[m', 'titulo':'\033[1;35m',
         'vermelho':'\033[31m', 'verde':'\033[32m', 'azul':'\033[34m'}

# Exibição do cabeçalho formatado no terminal
print('-=*=-'*10)
print(' '*18 , '{}EXERCICIO 41{}'.format(cores['titulo'], cores['limpa']))
print('-=*=-'*10)

# Solicita ao usuário o ano de nascimento
nascimento = int(input('Insira o seu ano de nascimento: '))

# Obtém o ano atual utilizando datetime
data_atual = datetime.datetime.now()
data = data_atual.date()
ano_atual = data.year

# Calcula a idade com base no ano de nascimento
idade = ano_atual - nascimento

# Verifica a categoria correspondente com base na idade
if idade <= 9:
    print('Idade: {}'.format(idade))
    print('Categoria {}MIRIM{}'.format(cores['titulo'], cores['limpa']))

elif idade > 9 and idade <= 14:
    print('Idade: {}'.format(idade))
    print('Categoria {}INFANTIL{}'.format(cores['titulo'], cores['limpa']))

elif idade > 14 and idade <= 19:
    print('Idade: {}'.format(idade))
    print('Categoria {}JUNIOR{}'.format(cores['titulo'], cores['limpa']))

elif idade == 20:
    print('Idade: {}'.format(idade))
    print('Categoria {}SÊNIOR{}'.format(cores['titulo'], cores['limpa']))

elif idade > 20:
    print('Idade: {}'.format(idade))
    print('Categoria {}MASTER{}'.format(cores['titulo'], cores['limpa']))
