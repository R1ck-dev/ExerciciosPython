cores = {'limpa':'\033[m', 'titulo':'\033[1;35m',
         'vermelho':'\033[31m', 'verde':'\033[32m', 'azul':'\033[34m'}

print('-=*=-'*10)
print(' '*18 , '{}EXERCICIO 42{}'.format(cores['titulo'], cores['limpa']))
print('-=*=-'*10)

a = int(input('Valor da reta A: '))
b = int(input('Valor da reta B: '))
c = int(input('Valor da reta C: '))

if (a + b) > c and (a + c) > b and (b + c) > a:
    print('\nPodem formar um triângulo!')
    if a == b and a == c and b == c:
        print('O triângulo formado será {}equilátero{}'.format(cores['titulo'], cores['limpa']))
    elif (a == b and a != c) or (a == c and a != b) or (b == c and b != a):
        print('O triângulo formado será {}isósceles{}'.format(cores['titulo'], cores['limpa']))
    elif a != b and a != c and b != c:
        print('O triângulo formado será {}escaleno{}'.format(cores['titulo'], cores['limpa']))
else:
    print('\nNão podem formar um triângulo!')