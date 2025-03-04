# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

# Solicita ao usuário um ano e armazena na variável 'ano'
ano = int(input('Insira o ano: '))

# Verifica se o ano é bissexto
if ano % 4 == 0:  # Um ano é bissexto se for divisível por 4
    if ano % 100 == 0:  # Porém, se for divisível por 100, pode não ser bissexto
        if ano % 400 == 0:  # Se também for divisível por 400, então é bissexto
            print('É um ano bissexto')
        else:  # Se for divisível por 100 mas não por 400, não é bissexto
            print('Não é um ano bissexto')
    else:  # Se for divisível por 4 mas não por 100, é bissexto
        print('É um ano bissexto')
else:  # Se não for divisível por 4, não é bissexto
    print('Não é um ano bissexto')
