# Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

# Define um dicionário com códigos ANSI para colorir a saída no terminal
cores = {'limpa':'\033[m', 'titulo':'\033[1;35m',
         'vermelho':'\033[31m', 'verde':'\033[32m', 'azul':'\033[34m'}

# Exibe um cabeçalho estilizado
print('-=*=-' * 10)
print(' ' * 18 , '{}EXERCICIO 61{}'.format(cores['titulo'], cores['limpa']))
print('-=*=-' * 10)

# Variável para controlar quantos novos termos serão mostrados (inicialmente diferente de 0)
termo_new = 1

# Solicita ao usuário o primeiro termo e a razão da progressão aritmética
primeiro_termo = int(input('Insira o primeiro termo da PA: '))
razao = int(input('Inisira a razão da PA: '))

# Inicializa o termo com o primeiro valor informado
termo = primeiro_termo

# Contador para controlar a exibição dos 10 primeiros termos
c = 0

# Exibe o primeiro termo da progressão
print('Progressão = {}{}{}'.format(cores['titulo'], primeiro_termo, cores['limpa']))

# Loop para exibir os 9 próximos termos da progressão (totalizando 10)
while c < 9:
    termo += razao  # Calcula o próximo termo
    print('Progressão = {}{}{}'.format(cores['titulo'], termo, cores['limpa']))
    c += 1  # Incrementa o contador

# Loop para permitir que o usuário solicite a exibição de mais termos
while termo_new != 0:
    print('Deseja mostrar mais quantos termos: ')
    termo_new = int(input())  # Usuário escolhe quantos termos adicionais deseja ver

    c = 0  # Reinicia o contador para controlar os novos termos
    while c < termo_new:
        termo += razao  # Calcula o próximo termo
        print('Progressão = {}{}{}'.format(cores['titulo'], termo, cores['limpa']))
        c += 1  # Incrementa o contador

# Mensagem de finalização do programa
print('{}---FINALIZADO---{}'.format(cores['vermelho'], cores['limpa']))
