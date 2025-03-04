# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.

# Dicionário contendo códigos ANSI para formatação de cores no terminal
cores = {'limpa':'\033[m', 'titulo':'\033[1;35m',
         'vermelho':'\033[31m', 'verde':'\033[32m', 'azul':'\033[34m'}

# Exibição do cabeçalho do exercício formatado com cores
print('-=*=-'*10)
print(' '*18 , '{}EXERCICIO 57{}'.format(cores['titulo'], cores['limpa']))
print('-=*=-'*10)

# Inicializa a variável 'sexo' como string vazia
sexo = ''

# Loop que continuará até que o usuário insira 'M' ou 'F'
while sexo != 'F' and sexo != 'M':
    sexo = input('Insira o sexo [F/M]: ').upper()  # Solicita entrada e converte para maiúscula
    print('Sexo informado {}[{}]{}.'.format(cores['titulo'], sexo, cores['limpa']))  # Exibe o valor inserido

# Mensagem final indicando que a entrada foi aceita
print('{}---FINALIZADO---{}'.format(cores['vermelho'], cores['limpa']))

