# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

# Dicionário com códigos ANSI para cores no terminal
cores = {'limpa':'\033[m', 'titulo':'\033[1;35m',
         'vermelho':'\033[31m', 'verde':'\033[32m', 'azul':'\033[34m'}

# Exibe um título estilizado no terminal
print('-=*=-'*10)
print(' '*18 , '{}EXERCICIO 36{}'.format(cores['titulo'], cores['limpa']))
print('-=*=-'*10)

# Solicita ao usuário os dados necessários para o cálculo
valor_casa = float(input('Insira o valor total da casa: '))
salario = float(input('Insira o seu salário: '))
qtd_anos = int(input('Em quantos anos pretende pagar a casa: '))

# Calcula o número total de meses do financiamento
meses = qtd_anos * 12
# Calcula o valor da parcela mensal
valor_mensal = valor_casa / meses
# Calcula 30% do salário do comprador
sal30porc = salario * 0.3

# Verifica se a prestação mensal excede 30% do salário
if valor_mensal > sal30porc:
    print('O valor mensal {}excede{} 30% do seu salário!'.format(cores['vermelho'], cores['limpa']))
    print('Valor mensal: R$ {:.2f}'.format(valor_mensal))
    print('30% do salário: R$ {:.2f}'.format(sal30porc))
else:
    print('O valor mensal {}não{} {}excede{} 30% do seu salário!'.format(cores['azul'], cores['limpa'],
                                                                             cores['azul'], cores['limpa']))
    print('Valor mensal: R$ {:.2f}'.format(valor_mensal))
    print('30% do salário: R$ {:.2f}'.format(sal30porc))
