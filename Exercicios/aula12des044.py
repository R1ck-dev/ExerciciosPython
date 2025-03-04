# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#
# – à vista dinheiro/cheque: 10% de desconto
#
# – à vista no cartão: 5% de desconto
#
# – em até 2x no cartão: preço formal
#
# – 3x ou mais no cartão: 20% de juros

# Dicionário contendo códigos ANSI para formatação de cores no terminal
cores = {'limpa':'\033[m', 'titulo':'\033[1;35m',
         'vermelho':'\033[31m', 'verde':'\033[32m', 'azul':'\033[34m'}

# Exibição do cabeçalho formatado no terminal
print('-=*=-'*10)
print(' '*18 , '{}EXERCICIO 44{}'.format(cores['titulo'], cores['limpa']))
print('-=*=-'*10)

# Solicita ao usuário o preço do item
preco = float(input('Insira o preço do item a ser pago: '))

# Exibe as opções de forma de pagamento
print('\n{}Forma de Pagamento:{}'.format(cores['azul'], cores['limpa']))
print('{}1 -{} À vista dinheiro/cheque'.format(cores['verde'], cores['limpa']))
print('{}2 -{} À vista no cartão'.format(cores['verde'], cores['limpa']))
print('{}3 -{} Até 2x no cartão'.format(cores['verde'], cores['limpa']))
print('{}4 -{} 3x ou mais no cartão\n'.format(cores['verde'], cores['limpa']))

# Solicita ao usuário a forma de pagamento escolhida
forma_pagamento = int(input('Indique a forma de pagamento: '))

# Condições para calcular o preço final com base na forma de pagamento escolhida
if forma_pagamento == 1:
    # 10% de desconto para pagamento à vista em dinheiro ou cheque
    print('\n{}10% de desconto{}'.format(cores['azul'], cores['limpa']))
    print('Preço Final: R$ {}{:.2f}{}'.format(cores['azul'], preco - (preco * 0.1), cores['limpa']))

elif forma_pagamento == 2:
    # 5% de desconto para pagamento à vista no cartão
    print('\n{}5% de desconto{}'.format(cores['azul'], cores['limpa']))
    print('Preço Final: R$ {}{:.2f}{}'.format(cores['azul'], preco - (preco * 0.05), cores['limpa']))

elif forma_pagamento == 3:
    # Pagamento em até 2x no cartão mantém o preço original
    print('\n{}Preço Normal{}'.format(cores['azul'], cores['limpa']))
    print('Preço Final: R$ {}{:.2f}{}'.format(cores['azul'], preco, cores['limpa']))

elif forma_pagamento == 4:
    # 20% de juros para pagamento parcelado em 3x ou mais no cartão
    print('\n{}20% de juros{}'.format(cores['vermelho'], cores['limpa']))
    print('Preço Final: R$ {}{:.2f}{}'.format(cores['vermelho'], preco + (preco * 0.2), cores['limpa']))

else:
    # Mensagem de erro para opções inválidas
    print('\nForma de Pagamento Inválida!')
