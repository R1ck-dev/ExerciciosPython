cores = {'limpa':'\033[m', 'titulo':'\033[1;35m',
         'vermelho':'\033[31m', 'verde':'\033[32m', 'azul':'\033[34m'}

print('-=*=-'*10)
print(' '*18 , '{}EXERCICIO 62{}'.format(cores['titulo'], cores['limpa']))
print('-=*=-'*10)

n_elementos = int(input('Insira quantos primeiros elementos da sequência serão mostrados: '))
c = 1
termo1 = 0
termo2 = 1
print('{}{}{} {}->{} {}{}{} {}->{}'.format(cores['titulo'], termo1, cores['limpa'],
                                   cores['vermelho'], cores['limpa'], cores['titulo'],
                                       termo1, cores['limpa'], cores['vermelho'], cores['limpa']), end='')
while c+2 <= n_elementos:
    termo3 = termo1 + termo2
    print(' {}{}{} {}->{}'.format(cores['titulo'], termo3, cores['limpa'],
                                  cores['vermelho'], cores['limpa']), end='')
    termo1 = termo2
    termo2 = termo3
    c += 1
print(' {}FIM{}'.format(cores['titulo'], cores['limpa']))