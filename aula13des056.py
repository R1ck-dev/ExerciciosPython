cores = {'limpa':'\033[m', 'titulo':'\033[1;35m',
         'vermelho':'\033[31m', 'verde':'\033[32m', 'azul':'\033[34m'}

print('-=*=-'*10)
print(' '*18 , '{}EXERCICIO 56{}'.format(cores['titulo'], cores['limpa']))
print('-=*=-'*10)

soma_idade = 0
qtd_mulheres = 0
homem_maisvelho = ''
homem_maisvelho_idade = 0

for c in range(0, 4):
    nome = input('Insira o seu nome: ')
    idade = int(input('Insira a sua idade: '))
    soma_idade += idade
    print('-=*=-' * 10)
    print('{}Indique o seu sexo:{}'.format(cores['vermelho'], cores['limpa']))
    print('1 --> Feminino')
    print('2 --> Masculino')
    print('-=*=-' * 10)
    sexo = int(input())
    if sexo == 1 and idade < 20:
        qtd_mulheres += 1
    elif sexo == 2 and idade > homem_maisvelho_idade:
        homem_maisvelho_idade = idade
        homem_maisvelho = nome
print('-=*=-'*10)
print('A média de idade do grupo é de {}{:.2f}{} ano(s)'.format(cores['titulo'], soma_idade/4, cores['limpa']))
print('O homem mais velho do grupo é o {}{}{}, tendo {}{}{} ano(s)'.format(cores['titulo'], homem_maisvelho, cores['limpa'],
                                                                           cores['titulo'], homem_maisvelho_idade, cores['limpa']))
print('No grupo, existem {}{}{} mulheres com menos de 20 anos'.format(cores['titulo'], qtd_mulheres, cores['limpa']))
print('-=*=-'*10)