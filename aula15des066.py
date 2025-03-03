cores = {'limpa':'\033[m', 'titulo':'\033[1;35m',
         'vermelho':'\033[31m', 'verde':'\033[32m', 'azul':'\033[34m'}

print('-=*=-'*10)
print(' '*18 , '{}EXERCICIO 66{}'.format(cores['titulo'], cores['limpa']))
print('-=*=-'*10)

n = cont = soma = 0
while True:
    n = int(input('Insira um valor qualquer: '))
    if n == 999:
        break
    soma += n
    cont += 1
print(f'A soma dos valores é {soma} e a quantidade de valores é {cont}')