ano = int(input('Insira o ano: '))
if ano%4 == 0:
    if ano%100 == 0:
        if ano%400 == 0:
            print('É um ano bissexto')
        else:
            print('Não é um ano bissexto')
    else:
        print('É um ano bissexto')
else:
    print('Não é um ano bissexto')