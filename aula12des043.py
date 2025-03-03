cores = {'limpa':'\033[m', 'titulo':'\033[1;35m',
         'vermelho':'\033[31m', 'verde':'\033[32m', 'azul':'\033[34m'}

print('-=*=-'*10)
print(' '*18 , '{}EXERCICIO 43{}'.format(cores['titulo'], cores['limpa']))
print('-=*=-'*10)

altura = (float(input('Insira a sua altura [em cm]: ')))/100
peso = float(input('Insira o seu peso: '))

imc = peso/altura**2

if imc < 18.5:
    print('\nIMC = {:.1f}'.format(imc))
    print('{}Abaixo{} do peso!'.format(cores['titulo'], cores['limpa']))
elif imc >= 18.5 and imc < 25:
    print('\nIMC = {:.1f}'.format(imc))
    print('Peso {}ideal{}!'.format(cores['titulo'], cores['limpa']))
elif imc >= 25 and imc < 30:
    print('\nIMC = {:.1f}'.format(imc))
    print('{}Sobrepeso{}!'.format(cores['titulo'], cores['limpa']))
elif imc >= 30 and imc < 40:
    print('\nIMC = {:.1f}'.format(imc))
    print('{}Obesidade{}!'.format(cores['titulo'], cores['limpa']))
elif imc > 40:
    print('\nIMC = {:.1f}'.format(imc))
    print('{}Obesidade mórbida{}!'.format(cores['titulo'], cores['limpa']))
