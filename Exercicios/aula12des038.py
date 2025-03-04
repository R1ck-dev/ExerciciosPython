# Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
#
# – O primeiro valor é maior
#
# – O segundo valor é maior
#
# – Não existe valor maior, os dois são iguais

# Dicionário contendo códigos ANSI para formatação de cores no terminal
cores = {'limpa':'\033[m', 'titulo':'\033[1;35m',
         'vermelho':'\033[31m', 'verde':'\033[32m', 'azul':'\033[34m'}

# Exibição do cabeçalho formatado
print('-=*=-'*10)
print(' '*18 , '{}EXERCICIO 38{}'.format(cores['titulo'], cores['limpa']))
print('-=*=-'*10)

# Solicitação de dois valores inteiros ao usuário
valor1 = int(input('Insira um valor qualquer: '))
valor2 = int(input('Insira um valor qualquer: '))

# Comparação entre os dois valores inseridos
if valor1 > valor2:
    # Se o primeiro valor for maior, exibe a mensagem correspondente
    print('{}{}{} é maior que {}{}{}'.format(cores['verde'], valor1, cores['limpa'],
                                             cores['vermelho'], valor2, cores['limpa']))
elif valor2 > valor1:
    # Se o segundo valor for maior, exibe a mensagem correspondente
    print('{}{}{} é maior que {}{}{}'.format(cores['verde'], valor2, cores['limpa'],
                                             cores['vermelho'], valor1, cores['limpa']))
else:
    # Se os valores forem iguais, exibe uma mensagem indicando isso
    print('Não existe valor maior, os dois são iguais!')
