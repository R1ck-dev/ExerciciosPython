# Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).

# Dicionário contendo códigos ANSI para formatação de cores no terminal
cores = {'limpa': '\033[m', 'titulo': '\033[1;35m',
         'vermelho': '\033[31m', 'verde': '\033[32m', 'azul': '\033[34m'}

# Exibição do cabeçalho formatado
print('-=*=-' * 10)
print(' ' * 18, '{}EXERCICIO 66{}'.format(cores['titulo'], cores['limpa']))
print('-=*=-' * 10)

# Inicialização das variáveis de controle
n = cont = soma = 0  # n: número inserido, cont: contador de valores, soma: soma dos valores

# Estrutura de repetição infinita (será interrompida com 'break' ao digitar 999)
while True:
    n = int(input('Insira um valor qualquer: '))  # Solicita um número ao usuário

    # Condição de parada: se o número for 999, sai do loop
    if n == 999:
        break

    # Atualiza a soma dos valores inseridos
    soma += n
    # Incrementa o contador de números digitados
    cont += 1

# Exibe os resultados finais, usando f-strings para formatação
print(f'A soma dos valores é {soma} e a quantidade de valores é {cont}')
