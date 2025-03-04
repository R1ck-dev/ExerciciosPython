# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

# Dicionário contendo códigos ANSI para formatação de cores no terminal
cores = {'limpa':'\033[m', 'titulo':'\033[1;35m',
         'vermelho':'\033[31m', 'verde':'\033[32m', 'azul':'\033[34m'}

# Exibição do cabeçalho do exercício formatado com cores
print('-=*=-'*10)
print(' '*18 , '{}EXERCICIO 52{}'.format(cores['titulo'], cores['limpa']))
print('-=*=-'*10)

# Solicita ao usuário um número inteiro para verificar se é primo
valor = int(input('Insira um valor qualquer: '))

# Variável de controle para determinar se o número é primo ou não
p_np = 0

# Laço que percorre os números de 2 até (valor - 1)
for c in range(2, valor):
    if valor % c == 0:  # Se o número for divisível por qualquer valor dentro do intervalo, ele não é primo
        p_np = 1  # Define a variável como 1 indicando que o número não é primo

# Verifica se houve alguma divisão exata além do 1 e do próprio número
if p_np != 0:
    print('{}{}{} {}não é primo{}'.format(cores['titulo'], valor, cores['limpa'],
                                            cores['vermelho'], cores['limpa']))
else:
    print('{}{}{} {}é primo{}'.format(cores['titulo'], valor, cores['limpa'],
                                            cores['azul'], cores['limpa']))

