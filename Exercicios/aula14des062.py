# Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.

# Define um dicionário com códigos ANSI para colorir a saída no terminal
cores = {'limpa':'\033[m', 'titulo':'\033[1;35m',
         'vermelho':'\033[31m', 'verde':'\033[32m', 'azul':'\033[34m'}

# Exibe um cabeçalho estilizado
print('-=*=-' * 10)
print(' ' * 18 , '{}EXERCICIO 62{}'.format(cores['titulo'], cores['limpa']))
print('-=*=-' * 10)

# Solicita ao usuário quantos elementos da sequência serão mostrados
n_elementos = int(input('Insira quantos primeiros elementos da sequência serão mostrados: '))

# Inicializa os primeiros termos da sequência de Fibonacci
c = 1
termo1 = 0
termo2 = 1

# Exibe os dois primeiros termos formatados com cores
print('{}{}{} {}->{} {}{}{} {}->{}'.format(cores['titulo'], termo1, cores['limpa'],
                                   cores['vermelho'], cores['limpa'], cores['titulo'],
                                       termo1, cores['limpa'], cores['vermelho'], cores['limpa']), end='')

# Loop para calcular e exibir os próximos termos da sequência até atingir a quantidade solicitada
while c+2 <= n_elementos:
    termo3 = termo1 + termo2  # Calcula o próximo termo da sequência
    print(' {}{}{} {}->{}'.format(cores['titulo'], termo3, cores['limpa'],
                                  cores['vermelho'], cores['limpa']), end='')

    # Atualiza os valores para a próxima iteração
    termo1 = termo2
    termo2 = termo3
    c += 1  # Incrementa o contador

# Mensagem de finalização do programa
print(' {}FIM{}'.format(cores['titulo'], cores['limpa']))
