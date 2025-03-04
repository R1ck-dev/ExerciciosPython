# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

# Dicionário contendo códigos ANSI para formatação de cores no terminal
cores = {'limpa':'\033[m', 'titulo':'\033[1;35m',
         'vermelho':'\033[31m', 'verde':'\033[32m', 'azul':'\033[34m'}

# Exibição do cabeçalho do exercício formatado com cores
print('-=*=-'*10)
print(' '*18 , '{}EXERCICIO 50{}'.format(cores['titulo'], cores['limpa']))
print('-=*=-'*10)

# Inicializa a variável soma que armazenará a soma dos números pares
soma = 0

# Laço que solicita ao usuário a inserção de 6 números inteiros
for c in range(0, 6):
    valor = int(input('Insira um valor qualquer: '))  # Lê o número digitado pelo usuário
    if valor % 2 == 0:  # Verifica se o número é par
        soma += valor  # Adiciona o número par à soma
        print('{}{}{} adicionado a soma.'.format(cores['azul'], valor, cores['limpa']))
    else:
        print('{}NÃO{} adicionado a soma.'.format(cores['vermelho'], cores['limpa']))  # Indica que o número ímpar foi ignorado

# Exibe a soma final de todos os números pares inseridos
print('Soma final = {}{}{}'.format(cores['titulo'], soma, cores['limpa']))
