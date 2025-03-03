cores = {'limpa':'\033[m', 'titulo':'\033[1;35m',
         'vermelho':'\033[31m', 'verde':'\033[32m', 'azul':'\033[34m'}

print('-=*=-'*10)
print(' '*18 , '{}EXERCICIO 44{}'.format(cores['titulo'], cores['limpa']))
print('-=*=-'*10)

preco = float(input('Insira o preço do item a ser pago: '))
print('\n{}Forma de Pagamento:{}'.format(cores['azul'], cores['limpa']))
print('{}1 -{} Á vista dinheiro/cheque'.format(cores['verde'], cores['limpa']))
print('{}2 -{} Á vista no cartão'.format(cores['verde'], cores['limpa']))
print('{}3 -{} Até 2x no cartão'.format(cores['verde'], cores['limpa']))
print('{}4 -{} 3x ou mais no cartão\n'.format(cores['verde'], cores['limpa']))
forma_pagamento = int(input('Indique a forma de pagamento: '))

if forma_pagamento == 1:
    print('\n{}10% de desconto{}'.format(cores['azul'], cores['limpa']))
    print('Preço Final: R$ {}{:.2f}{}'.format(cores['azul'], preco-(preco*0.1), cores['limpa']))
elif forma_pagamento == 2:
    print('\n{}5% de desconto{}'.format(cores['azul'], cores['limpa']))
    print('Preço Final: R$ {}{:.2f}{}'.format(cores['azul'], preco - (preco * 0.05), cores['limpa']))
elif forma_pagamento == 3:
    print('\n{}Preço Normal{}'.format(cores['azul'], cores['limpa']))
    print('Preço Final: R$ {}{:.2f}{}'.format(cores['azul'], preco, cores['limpa']))
elif forma_pagamento == 4:
    print('\n{}20% de juros{}'.format(cores['vermelho'], cores['limpa']))
    print('Preço Final: R$ {}{:.2f}{}'.format(cores['vermelho'], preco + (preco * 0.2), cores['limpa']))
else:
    print('\nForma de Pagamento Inválida!')