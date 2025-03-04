# Crie um programa que leia dois valores e mostre um menu na tela:
#
# [ 1 ] somar
#
# [ 2 ] multiplicar
#
# [ 3 ] maior
#
# [ 4 ] novos números
#
# [ 5 ] sair do programa

# Importa um dicionário com códigos ANSI para colorir o terminal
cores = {'limpa':'\033[m', 'titulo':'\033[1;35m',
         'vermelho':'\033[31m', 'verde':'\033[32m', 'azul':'\033[34m'}

# Exibe um cabeçalho estilizado
print('-=*=-' * 10)
print(' ' * 18 , '{}EXERCICIO 59{}'.format(cores['titulo'], cores['limpa']))
print('-=*=-' * 10)

# Inicializa a variável que controla a escolha do menu
menu_entrada = 0

# Enquanto o usuário não escolher a opção de sair (5), o programa continuará rodando
while menu_entrada != 5:

    # Solicita ao usuário que insira dois valores numéricos
    valor1 = float(input('Insira o primeiro valor: '))
    valor2 = float(input('Insira o segundo valor: '))
    maior = 0  # Variável inicializada, mas não é usada diretamente depois

    # Exibe o menu de opções
    print('{}--- MENU ---{}'.format(cores['titulo'], cores['limpa']))
    print('{}[1]{} Somar'.format(cores['titulo'], cores['limpa']))
    print('{}[2]{} Multiplicar'.format(cores['titulo'], cores['limpa']))
    print('{}[3]{} Maior'.format(cores['titulo'], cores['limpa']))
    print('{}[4]{} Novos Números'.format(cores['titulo'], cores['limpa']))
    print('{}[5]{} Sair do Programa'.format(cores['titulo'], cores['limpa']))
    print('{}------------{}'.format(cores['titulo'], cores['limpa']))

    # Solicita que o usuário escolha uma opção do menu
    menu_entrada = int(input())

    # Linha divisória para organização visual
    print('{}------------{}'.format(cores['titulo'], cores['limpa']))

    # Se o usuário escolher a opção 1, realiza a soma dos valores e exibe o resultado
    if menu_entrada == 1:
        print('{}{}{} + {}{}{}'.format(cores['azul'], valor1, cores['limpa'],
                                       cores['azul'], valor2, cores['limpa']))
        print('Resultado --> {}{}{}'.format(cores['azul'], valor1 + valor2, cores['limpa']))
        print('{}------------{}'.format(cores['titulo'], cores['limpa']))

    # Se o usuário escolher a opção 2, realiza a multiplicação dos valores e exibe o resultado
    elif menu_entrada == 2:
        print('{}{}{} x {}{}{}'.format(cores['azul'], valor1, cores['limpa'],
                                       cores['azul'], valor2, cores['limpa']))
        print('Resultado --> {}{}{}'.format(cores['azul'], valor1 * valor2, cores['limpa']))
        print('{}------------{}'.format(cores['titulo'], cores['limpa']))

    # Se o usuário escolher a opção 3, verifica qual número é maior e exibe o resultado
    elif menu_entrada == 3:
        if valor1 > valor2:
            print('{}{}{} > {}{}{}'.format(cores['azul'], valor1, cores['limpa'],
                                           cores['azul'], valor2, cores['limpa']))
            print('{}------------{}'.format(cores['titulo'], cores['limpa']))
        else:
            print('{}{}{} > {}{}{}'.format(cores['azul'], valor2, cores['limpa'],
                                           cores['azul'], valor1, cores['limpa']))
            print('{}------------{}'.format(cores['titulo'], cores['limpa']))

    # Se o usuário escolher a opção 4, solicita novamente os números e exibe o menu novamente
    if menu_entrada == 4:
        valor1 = float(input('Insira o {}[novo]{} primeiro valor: '.format(cores['vermelho'], cores['limpa'])))
        valor2 = float(input('Insira o {}[novo]{} segundo valor: '.format(cores['vermelho'], cores['limpa'])))

        # Exibe novamente o menu de opções
        print('{}--- MENU ---{}'.format(cores['titulo'], cores['limpa']))
        print('{}[1]{} Somar'.format(cores['titulo'], cores['limpa']))
        print('{}[2]{} Multiplicar'.format(cores['titulo'], cores['limpa']))
        print('{}[3]{} Maior'.format(cores['titulo'], cores['limpa']))
        print('{}[4]{} Novos Números'.format(cores['titulo'], cores['limpa']))
        print('{}[5]{} Sair do Programa'.format(cores['titulo'], cores['limpa']))
        print('{}------------{}'.format(cores['titulo'], cores['limpa']))

        # Solicita uma nova escolha de menu
        menu_entrada = int(input())
        print('{}------------{}'.format(cores['titulo'], cores['limpa']))

        # Se a nova escolha for soma, exibe o resultado
        if menu_entrada == 1:
            print('{}{}{} + {}{}{}'.format(cores['azul'], valor1, cores['limpa'],
                                           cores['azul'], valor2, cores['limpa']))
            print('Resultado --> {}{}{}'.format(cores['azul'], valor1+valor2, cores['limpa']))
            print('{}------------{}'.format(cores['titulo'], cores['limpa']))

        # Se a nova escolha for multiplicação, exibe o resultado
        elif menu_entrada == 2:
            print('{}{}{} x {}{}{}'.format(cores['azul'], valor1, cores['limpa'],
                                           cores['azul'], valor2, cores['limpa']))
            print('Resultado --> {}{}{}'.format(cores['azul'], valor1 * valor2, cores['limpa']))
            print('{}------------{}'.format(cores['titulo'], cores['limpa']))

        # Se a nova escolha for "maior número", exibe o resultado
        elif menu_entrada == 3:
            if valor1 > valor2:
                print('{}{}{} > {}{}{}'.format(cores['azul'], valor1, cores['limpa'],
                                           cores['azul'], valor2, cores['limpa']))
                print('{}------------{}'.format(cores['titulo'], cores['limpa']))
            else:
                print('{}{}{} > {}{}{}'.format(cores['azul'], valor2, cores['limpa'],
                                               cores['azul'], valor1, cores['limpa']))
                print('{}------------{}'.format(cores['titulo'], cores['limpa']))

# Quando o usuário escolhe a opção 5, o programa exibe a mensagem de finalização
print('{}Programa Finalizado{}'.format(cores['verde'], cores['limpa']))
