# Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

# Dicionário contendo códigos ANSI para formatação de cores no terminal
cores = {'limpa':'\033[m', 'titulo':'\033[1;35m',
         'vermelho':'\033[31m', 'verde':'\033[32m', 'azul':'\033[34m'}

# Exibição de um cabeçalho estilizado para o exercício
print('-=*=-'*10)
print(' '*18 , '{}EXERCICIO 37{}'.format(cores['titulo'], cores['limpa']))
print('-=*=-'*10)

# Solicita ao usuário um número inteiro para conversão
decimal = int(input('Insira o valor decimal: '))

# Exibe as opções de conversão disponíveis
print('\n{}Indique a conversão:{}'.format(cores['azul'], cores['limpa']))
print('{}1 --> Binário{}'.format(cores['verde'], cores['limpa']))
print('{}2 --> Octal{}'.format(cores['verde'], cores['limpa']))
print('{}3 --> Hexadecimal{}'.format(cores['verde'], cores['limpa']))

# Lê a opção escolhida pelo usuário
s_n = int(input('\nIndique: '))

# Realiza a conversão com base na escolha do usuário
if s_n == 1:
    # Conversão para binário (bin()) e remoção do prefixo '0b'
    print('\n{} convertido para binário --> {}{}{}'.format(decimal, cores['azul'], bin(decimal)[2:], cores['limpa']))
elif s_n == 2:
    # Conversão para octal (oct()) e remoção do prefixo '0o'
    print('\n{} convertido para octal --> {}{}{}'.format(decimal, cores['azul'], oct(decimal)[2:], cores['limpa']))
elif s_n == 3:
    # Conversão para hexadecimal (hex()) e remoção do prefixo '0x'
    print('\n{} convertido para hexadecimal --> {}{}{}'.format(decimal, cores['azul'], hex(decimal)[2:], cores['limpa']))
else:
    # Mensagem de erro caso o usuário insira uma opção inválida
    print('\n{}Opção inválida!{}'.format(cores['vermelho'], cores['limpa']))
