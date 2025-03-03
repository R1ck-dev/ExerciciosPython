cores = {'limpa':'\033[m', 'titulo':'\033[1;35m',
         'vermelho':'\033[31m', 'verde':'\033[32m', 'azul':'\033[34m'}

print('-=*=-'*10)
print(' '*18 , '{}EXERCICIO 55{}'.format(cores['titulo'], cores['limpa']))
print('-=*=-'*10)

maior = menor = float(input('Insira o peso da 1ª pessoa: '))

for c in range(1, 5):
    peso = float(input(f'Insira o peso da {c+1}ª pessoa: '))
    if peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso
print('{}{}{} foi o {}maior peso{}'.format(cores['titulo'], maior, cores['limpa'],
                                           cores['vermelho'], cores['limpa']))
print('{}{}{} foi o {}menor peso{}'.format(cores['titulo'], menor, cores['limpa'],
                                           cores['azul'], cores['limpa']))