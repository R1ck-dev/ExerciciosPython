cores = {'limpa':'\033[m', 'titulo':'\033[1;35m',
         'vermelho':'\033[31m', 'verde':'\033[32m', 'azul':'\033[34m'}

print('-=*=-'*10)
print(' '*18 , '{}EXERCICIO 59{}'.format(cores['titulo'], cores['limpa']))
print('-=*=-'*10)

menu_entrada = 0

while menu_entrada != 5:

    valor1 = float(input('Insira o primeiro valor: '))
    valor2 = float(input('Insira o segundo valor: '))
    maior = 0

    print('{}--- MENU ---{}'.format(cores['titulo'], cores['limpa']))
    print('{}[1]{} Somar'.format(cores['titulo'], cores['limpa']))
    print('{}[2]{} Multiplicar'.format(cores['titulo'], cores['limpa']))
    print('{}[3]{} Maior'.format(cores['titulo'], cores['limpa']))
    print('{}[4]{} Novos Números'.format(cores['titulo'], cores['limpa']))
    print('{}[5]{} Sair do Programa'.format(cores['titulo'], cores['limpa']))
    print('{}------------{}'.format(cores['titulo'], cores['limpa']))
    menu_entrada = int(input())
    print('{}------------{}'.format(cores['titulo'], cores['limpa']))

    if menu_entrada == 1:
        print('{}{}{} + {}{}{}'.format(cores['azul'], valor1, cores['limpa'],
                                       cores['azul'], valor2, cores['limpa']))
        print('Resultado --> {}{}{}'.format(cores['azul'], valor1 + valor2, cores['limpa']))
        print('{}------------{}'.format(cores['titulo'], cores['limpa']))
    elif menu_entrada == 2:
        print('{}{}{} x {}{}{}'.format(cores['azul'], valor1, cores['limpa'],
                                       cores['azul'], valor2, cores['limpa']))
        print('Resultado --> {}{}{}'.format(cores['azul'], valor1 * valor2, cores['limpa']))
        print('{}------------{}'.format(cores['titulo'], cores['limpa']))
    elif menu_entrada == 3:
        if valor1 > valor2:
            print('{}{}{} > {}{}{}'.format(cores['azul'], valor1, cores['limpa'],
                                           cores['azul'], valor2, cores['limpa']))
            print('{}------------{}'.format(cores['titulo'], cores['limpa']))
        else:
            print('{}{}{} > {}{}{}'.format(cores['azul'], valor2, cores['limpa'],
                                           cores['azul'], valor1, cores['limpa']))
            print('{}------------{}'.format(cores['titulo'], cores['limpa']))

    if menu_entrada == 4:
        valor1 = float(input('Insira o {}[novo]{} primeiro valor: '.format(cores['vermelho'], cores['limpa'])))
        valor2 = float(input('Insira o {}[novo]{} segundo valor: '.format(cores['vermelho'], cores['limpa'])))

        print('{}--- MENU ---{}'.format(cores['titulo'], cores['limpa']))
        print('{}[1]{} Somar'.format(cores['titulo'], cores['limpa']))
        print('{}[2]{} Multiplicar'.format(cores['titulo'], cores['limpa']))
        print('{}[3]{} Maior'.format(cores['titulo'], cores['limpa']))
        print('{}[4]{} Novos Números'.format(cores['titulo'], cores['limpa']))
        print('{}[5]{} Sair do Programa'.format(cores['titulo'], cores['limpa']))
        print('{}------------{}'.format(cores['titulo'], cores['limpa']))
        menu_entrada = int(input())
        print('{}------------{}'.format(cores['titulo'], cores['limpa']))

        if menu_entrada == 1:
            print('{}{}{} + {}{}{}'.format(cores['azul'], valor1, cores['limpa'],
                                           cores['azul'], valor2, cores['limpa']))
            print('Resultado --> {}{}{}'.format(cores['azul'], valor1+valor2, cores['limpa']))
            print('{}------------{}'.format(cores['titulo'], cores['limpa']))
        elif menu_entrada == 2:
            print('{}{}{} x {}{}{}'.format(cores['azul'], valor1, cores['limpa'],
                                           cores['azul'], valor2, cores['limpa']))
            print('Resultado --> {}{}{}'.format(cores['azul'], valor1 * valor2, cores['limpa']))
            print('{}------------{}'.format(cores['titulo'], cores['limpa']))
        elif menu_entrada == 3:
            if valor1 > valor2:
                print('{}{}{} > {}{}{}'.format(cores['azul'], valor1, cores['limpa'],
                                           cores['azul'], valor2, cores['limpa']))
                print('{}------------{}'.format(cores['titulo'], cores['limpa']))
            else:
                print('{}{}{} > {}{}{}'.format(cores['azul'], valor2, cores['limpa'],
                                               cores['azul'], valor1, cores['limpa']))
                print('{}------------{}'.format(cores['titulo'], cores['limpa']))

print('{}Programa Finalizado{}'.format(cores['verde'], cores['limpa']))

