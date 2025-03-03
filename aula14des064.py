cores = {'limpa':'\033[m', 'titulo':'\033[1;35m',
         'vermelho':'\033[31m', 'verde':'\033[32m', 'azul':'\033[34m'}

print('-=*=-'*10)
print(' '*18 , '{}EXERCICIO 64{}'.format(cores['titulo'], cores['limpa']))
print('-=*=-'*10)

# Entrada do primeiro valor
valor = int(input('Insira um valor: '))

# Inicializando variáveis
soma = valor
cont = 1
maior = valor
menor = valor

# Perguntar se deseja continuar
resp = input('Deseja continuar [S/N]?: ').upper()

while resp == 'S':
    valor = int(input('Insira um valor: '))
    soma += valor
    cont += 1
    if valor > maior:
        maior = valor
    if valor < menor:
        menor = valor
    resp = input('Deseja continuar [S/N]?: ').upper()

# Resultado final
print('Você digitou {} números, e a média foi {:.2f}'.format(cont, soma / cont))
print('O maior valor digitado foi {} e o menor foi {}'.format(maior, menor))
