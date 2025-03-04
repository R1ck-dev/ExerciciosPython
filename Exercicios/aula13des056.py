# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

# Dicionário contendo códigos ANSI para formatação de cores no terminal
cores = {'limpa': '\033[m', 'titulo': '\033[1;35m',
         'vermelho': '\033[31m', 'verde': '\033[32m', 'azul': '\033[34m'}

# Exibição do cabeçalho do exercício formatado com cores
print('-=*=-' * 10)
print(' ' * 18, '{}EXERCICIO 56{}'.format(cores['titulo'], cores['limpa']))
print('-=*=-' * 10)

# Inicialização das variáveis para armazenar os dados do grupo
soma_idade = 0  # Soma das idades para calcular a média
qtd_mulheres = 0  # Contador de mulheres com menos de 20 anos
homem_maisvelho = ''  # Nome do homem mais velho
homem_maisvelho_idade = 0  # Idade do homem mais velho

# Loop para coletar informações de 4 pessoas
for c in range(0, 4):
    nome = input('Insira o seu nome: ')  # Entrada do nome
    idade = int(input('Insira a sua idade: '))  # Entrada da idade
    soma_idade += idade  # Soma da idade ao total para cálculo da média

    # Exibição do menu de seleção do sexo
    print('-=*=-' * 10)
    print('{}Indique o seu sexo:{}'.format(cores['vermelho'], cores['limpa']))
    print('1 --> Feminino')
    print('2 --> Masculino')
    print('-=*=-' * 10)

    sexo = int(input())  # Entrada do sexo (1 para feminino, 2 para masculino)

    # Verifica se a pessoa é mulher e tem menos de 20 anos
    if sexo == 1 and idade < 20:
        qtd_mulheres += 1

    # Verifica se a pessoa é homem e se é o mais velho registrado até o momento
    elif sexo == 2 and idade > homem_maisvelho_idade:
        homem_maisvelho_idade = idade
        homem_maisvelho = nome

# Exibição dos resultados
print('-=*=-' * 10)
print('A média de idade do grupo é de {}{:.2f}{} ano(s)'.format(cores['titulo'], soma_idade / 4, cores['limpa']))
print('O homem mais velho do grupo é o {}{}{}, tendo {}{}{} ano(s)'.format(cores['titulo'], homem_maisvelho,
                                                                           cores['limpa'],
                                                                           cores['titulo'], homem_maisvelho_idade,
                                                                           cores['limpa']))
print('No grupo, existem {}{}{} mulheres com menos de 20 anos'.format(cores['titulo'], qtd_mulheres, cores['limpa']))
print('-=*=-' * 10)
