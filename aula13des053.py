cores = {'limpa':'\033[m', 'titulo':'\033[1;35m',
         'vermelho':'\033[31m', 'verde':'\033[32m', 'azul':'\033[34m'}

print('-=*=-'*10)
print(' '*18 , '{}EXERCICIO 53{}'.format(cores['titulo'], cores['limpa']))
print('-=*=-'*10)

frase = input('Insira a frase a ser analisada: ').replace(' ', '')
frase_contrario = ''

for c in range(len(frase) - 1, -1, -1):
    #frase_contrario[i] = frase[c] --> O problema é que em Python, strings são imutáveis. Isso significa
    # que você não pode modificar diretamente os caracteres de uma string usando índices

    frase_contrario += frase[c]

if frase == frase_contrario:
    print('{}São Palíndromos!{}'.format(cores['verde'], cores['limpa']))
else:
    print('{}Não são Palíndromos!{}'.format(cores['vermelho'], cores['limpa']))

print('-=*=-'*10)
print(frase)
print(frase_contrario)
