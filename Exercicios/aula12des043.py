# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
#
# – IMC abaixo de 18,5: Abaixo do Peso
#
# – Entre 18,5 e 25: Peso Ideal
#
# – 25 até 30: Sobrepeso
#
# – 30 até 40: Obesidade
#
# – Acima de 40: Obesidade Mórbida

# Dicionário contendo códigos ANSI para formatação de cores no terminal
cores = {'limpa':'\033[m', 'titulo':'\033[1;35m',
         'vermelho':'\033[31m', 'verde':'\033[32m', 'azul':'\033[34m'}

# Exibição do cabeçalho formatado no terminal
print('-=*=-'*10)
print(' '*18 , '{}EXERCICIO 43{}'.format(cores['titulo'], cores['limpa']))
print('-=*=-'*10)

# Solicita ao usuário sua altura e converte de cm para metros
altura = (float(input('Insira a sua altura [em cm]: ')))/100

# Solicita ao usuário seu peso
peso = float(input('Insira o seu peso: '))

# Cálculo do Índice de Massa Corporal (IMC)
imc = peso / altura**2

# Exibe o IMC e classifica de acordo com a tabela
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
