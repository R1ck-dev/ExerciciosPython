# Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.

# Dicionário contendo códigos ANSI para formatação de cores no terminal
cores = {'limpa':'\033[m', 'titulo':'\033[1;35m',
         'vermelho':'\033[31m', 'verde':'\033[32m', 'azul':'\033[34m'}

# Exibição do cabeçalho do exercício formatado com cores
print('-=*=-'*10)
print(' '*18 , '{}EXERCICIO 47{}'.format(cores['titulo'], cores['limpa']))
print('-=*=-'*10)

# Loop que percorre os números de 1 a 50 (incluindo o 50)
for c in range (1, 51):
    if c % 2 == 0:  # Verifica se o número é par (divisível por 2)
        # Exibe o número par formatado com cores
        print('{}{}{} é {}par{}!'.format(cores['titulo'], c, cores['limpa'],
                                         cores['vermelho'], cores['limpa']))

