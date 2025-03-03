cores = {'limpa':'\033[m', 'titulo':'\033[1;35m',
         'vermelho':'\033[31m', 'verde':'\033[32m', 'azul':'\033[34m'}

print('-=*=-'*10)
print(' '*18 , '{}EXERCICIO 40{}'.format(cores['titulo'], cores['limpa']))
print('-=*=-'*10)

nota1 = float(input('Insira a nota 1: '))
nota2 = float(input('Insira a nota 2: '))

media = (nota1+nota2)/2

if media < 5:
    print('Média: {:.2}'.format(media))
    print('{}REPROVADO!{}'.format(cores['vermelho'], cores['limpa']))
elif media >= 5 and media < 7:
    print('Média: {:.2}'.format(media))
    print('{}RECUPERAÇÃO!{}'.format(cores['azul'], cores['limpa']))
elif media >= 7:
    print('Média: {:.2}'.format(media))
    print('{}APROVADO!{}'.format(cores['verde'], cores['limpa']))