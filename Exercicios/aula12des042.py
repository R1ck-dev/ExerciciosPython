# Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#
# – EQUILÁTERO: todos os lados iguais
#
# – ISÓSCELES: dois lados iguais, um diferente
#
# – ESCALENO: todos os lados diferentes

# Dicionário contendo códigos ANSI para formatação de cores no terminal
cores = {'limpa':'\033[m', 'titulo':'\033[1;35m',
         'vermelho':'\033[31m', 'verde':'\033[32m', 'azul':'\033[34m'}

# Exibição do cabeçalho formatado no terminal
print('-=*=-'*10)
print(' '*18 , '{}EXERCICIO 42{}'.format(cores['titulo'], cores['limpa']))
print('-=*=-'*10)

# Solicita ao usuário os comprimentos das três retas
a = int(input('Valor da reta A: '))
b = int(input('Valor da reta B: '))
c = int(input('Valor da reta C: '))

# Verifica se as retas podem formar um triângulo usando a condição da desigualdade triangular
if (a + b) > c and (a + c) > b and (b + c) > a:
    print('\nPodem formar um triângulo!')

    # Verifica o tipo de triângulo baseado nos comprimentos das retas
    if a == b and a == c and b == c:
        print('O triângulo formado será {}equilátero{}'.format(cores['titulo'], cores['limpa']))  # Todos os lados iguais

    elif (a == b and a != c) or (a == c and a != b) or (b == c and b != a):
        print('O triângulo formado será {}isósceles{}'.format(cores['titulo'], cores['limpa']))  # Dois lados iguais, um diferente

    elif a != b and a != c and b != c:
        print('O triângulo formado será {}escaleno{}'.format(cores['titulo'], cores['limpa']))  # Todos os lados diferentes

else:
    print('\nNão podem formar um triângulo!')  # Caso as retas não satisfaçam a condição da desigualdade triangular
