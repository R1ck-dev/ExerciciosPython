cores = {'limpa':'\033[m', 'titulo':'\033[1;35m',
         'vermelho':'\033[31m', 'verde':'\033[32m', 'azul':'\033[34m'}

print('-=*=-'*10)
print(' '*18 , '{}EXERCICIO 61{}'.format(cores['titulo'], cores['limpa']))
print('-=*=-'*10)

termo_new = 1

primeiro_termo = int(input('Insira o primeiro termo da PA: '))
razao = int(input('Inisira a razão da PA: '))
termo = primeiro_termo
c = 0

print('Progressão = {}{}{}'.format(cores['titulo'], primeiro_termo, cores['limpa']))

while c < 9:
    termo += razao
    print('Progressão = {}{}{}'.format(cores['titulo'], termo, cores['limpa']))
    c += 1

while termo_new != 0:
    print('Deseja mostrar mais quantos termos: ')
    termo_new = int(input())

    c = 0
    while c < termo_new:
        termo += razao
        print('Progressão = {}{}{}'.format(cores['titulo'], termo, cores['limpa']))
        c += 1
print('{}---FINALIZADO---{}'.format(cores['vermelho'],cores['limpa']))