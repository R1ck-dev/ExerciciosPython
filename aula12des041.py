import datetime

cores = {'limpa':'\033[m', 'titulo':'\033[1;35m',
         'vermelho':'\033[31m', 'verde':'\033[32m', 'azul':'\033[34m'}

print('-=*=-'*10)
print(' '*18 , '{}EXERCICIO 41{}'.format(cores['titulo'], cores['limpa']))
print('-=*=-'*10)

nascimento = int(input('Insira o seu ano de nascimento: '))
data_atual = datetime.datetime.now()
data = data_atual.date()
ano_atual = data.year
idade = ano_atual-nascimento

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