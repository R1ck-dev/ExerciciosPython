# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

# Dicionário contendo códigos ANSI para formatação de cores no terminal
cores = {'limpa':'\033[m', 'titulo':'\033[1;35m',
         'vermelho':'\033[31m', 'verde':'\033[32m', 'azul':'\033[34m'}

# Exibição do cabeçalho do exercício formatado com cores
print('-=*=-'*10)
print(' '*18 , '{}EXERCICIO 51{}'.format(cores['titulo'], cores['limpa']))
print('-=*=-'*10)

# Solicita ao usuário o primeiro termo da progressão aritmética (PA)
primeiro_termo = int(input('Insira o primeiro termo da PA: '))

# Solicita ao usuário a razão da PA
razao = int(input('Inisira a razão da PA: '))

# Inicializa a variável que armazena o termo atual da PA
termo = primeiro_termo

# Exibe o primeiro termo da PA
print('Progressão = {}{}{}'.format(cores['titulo'], primeiro_termo, cores['limpa']))

# Laço para calcular e exibir os próximos 9 termos da PA
for c in range(0, 9):  # Começa em 0 e executa 9 iterações, totalizando 10 termos com o primeiro já exibido
    termo += razao  # Calcula o próximo termo da PA somando a razão
    print('Progressão = {}{}{}'.format(cores['titulo'], termo, cores['limpa']))  # Exibe o termo atual da PA
