# Faça um programa que leia um número qualquer e mostre o seu fatorial.

# Define um dicionário com códigos ANSI para colorir a saída no terminal
cores = {'limpa':'\033[m', 'titulo':'\033[1;35m',
         'vermelho':'\033[31m', 'verde':'\033[32m', 'azul':'\033[34m'}

# Exibe um cabeçalho estilizado
print('-=*=-' * 10)
print(' ' * 18 , '{}EXERCICIO 60{}'.format(cores['titulo'], cores['limpa']))
print('-=*=-' * 10)

# Solicita ao usuário um número inteiro e inicializa a variável 'multiplicador' com esse valor
multiplicador = valor = int(input('Insira o valor: '))

# Inicializa a variável 'valor_novo' como 1, que será usada para calcular o fatorial
valor_novo = 1

# Laço de repetição para calcular o fatorial do número inserido
while multiplicador > 1:
    valor_novo *= multiplicador  # Multiplica o valor acumulado pelo multiplicador atual
    multiplicador -= 1  # Decrementa o multiplicador

# Exibe o resultado do fatorial com formatação colorida
print('{}{}!{} = {}{}{}'.format(cores['vermelho'], valor, cores['limpa'],
                                cores['azul'], valor_novo, cores['limpa']))
