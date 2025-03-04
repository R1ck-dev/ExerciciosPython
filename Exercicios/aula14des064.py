# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

# Dicionário para armazenar códigos de cores ANSI, usados para formatar a saída no terminal
cores = {'limpa': '\033[m', 'titulo': '\033[1;35m',
         'vermelho': '\033[31m', 'verde': '\033[32m', 'azul': '\033[34m'}

# Exibição do cabeçalho formatado
print('-=*=-' * 10)
print(' ' * 18, '{}EXERCICIO 64{}'.format(cores['titulo'], cores['limpa']))
print('-=*=-' * 10)

# Solicita ao usuário o primeiro valor
valor = int(input('Insira um valor: '))

# Inicializa as variáveis de controle
soma = valor  # Armazena a soma dos valores digitados
cont = 1  # Conta a quantidade de números inseridos
maior = valor  # Guarda o maior número inserido
menor = valor  # Guarda o menor número inserido

# Pergunta se o usuário deseja continuar inserindo números
resp = input('Deseja continuar [S/N]?: ').upper()

# Loop continua enquanto o usuário responder 'S'
while resp == 'S':
    valor = int(input('Insira um valor: '))  # Solicita um novo valor
    soma += valor  # Soma o novo valor ao total
    cont += 1  # Incrementa o contador

    # Verifica se o novo valor é o maior já inserido
    if valor > maior:
        maior = valor

    # Verifica se o novo valor é o menor já inserido
    if valor < menor:
        menor = valor

    # Pergunta novamente se deseja continuar
    resp = input('Deseja continuar [S/N]?: ').upper()

# Exibe os resultados finais
print('Você digitou {} números, e a média foi {:.2f}'.format(cont, soma / cont))
print('O maior valor digitado foi {} e o menor foi {}'.format(maior, menor))

