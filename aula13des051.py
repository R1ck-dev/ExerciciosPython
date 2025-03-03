cores = {'limpa':'\033[m', 'titulo':'\033[1;35m',
         'vermelho':'\033[31m', 'verde':'\033[32m', 'azul':'\033[34m'}

print('-=*=-'*10)
print(' '*18 , '{}EXERCICIO 51{}'.format(cores['titulo'], cores['limpa']))
print('-=*=-'*10)

primeiro_termo = int(input('Insira o primeiro termo da PA: '))
razao = int(input('Inisira a razão da PA: '))
termo = primeiro_termo

print('Progressão = {}{}{}'.format(cores['titulo'], primeiro_termo, cores['limpa']))

for c in range(0, 9):
    termo += razao
    print('Progressão = {}{}{}'.format(cores['titulo'], termo, cores['limpa']))
