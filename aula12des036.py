cores = {'limpa':'\033[m', 'titulo':'\033[1;35m',
         'vermelho':'\033[31m', 'verde':'\033[32m', 'azul':'\033[34m'}

print('-=*=-'*10)
print(' '*18 , '{}EXERCICIO 36{}'.format(cores['titulo'], cores['limpa']))
print('-=*=-'*10)

valor_casa = float(input('Insira o valor total da casa: '))
salario = float(input('Insira o seu salário: '))
qtd_anos = int(input('Em quantos anos pretende pagar a casa: '))

meses = qtd_anos*12
valor_mensal = valor_casa/meses
sal30porc = salario*0.3

if valor_mensal > sal30porc:
    print('O valor mensal {}excede{} 30% do seu salário!'.format(cores['vermelho'], cores['limpa']))
    print('Valor mensal: R$ {:.2f}'.format(valor_mensal))
    print('30% do salário: R$ {:.2f}'.format((sal30porc)))
else:
    print('O valor mensal {}não{} {}excede{} 30% do seu salário!'.format(cores['azul'], cores['limpa'],
                                                                             cores['azul'], cores['limpa']))
    print('Valor mensal: R$ {:.2f}'.format(valor_mensal))
    print('30% do salário: R$ {:.2f}'.format((sal30porc)))