# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.

# Dicionário contendo códigos ANSI para formatação de cores no terminal
cores = {'limpa':'\033[m', 'titulo':'\033[1;35m',
         'vermelho':'\033[31m', 'verde':'\033[32m', 'azul':'\033[34m'}

# Exibição do cabeçalho formatado
print('-=*=-' * 10)
print(' ' * 18 , '{}EXERCICIO 67{}'.format(cores['titulo'], cores['limpa']))
print('-=*=-' * 10)

# Loop principal para exibição das tabuadas
while True:
    # Solicita ao usuário um número para mostrar a tabuada
    valor = int(input('Deseja ver a tabuada de qual número: '))

    # Se o número for negativo, interrompe o loop e finaliza o programa
    if valor < 0:
        break

    # Inicializa o multiplicador da tabuada
    multiplicador = 1

    # Exibe uma linha decorativa antes da tabuada
    print('{}-=*=-{}'.format(cores['verde'], cores['limpa']) * 10)

    # Loop para calcular e exibir a tabuada de 1 a 10
    while multiplicador <= 10:
        print('{}{}{} x {} = {}{}{}'.format(cores['vermelho'], multiplicador, cores['limpa'],
                                            valor, cores['titulo'], valor * multiplicador, cores['limpa']))
        multiplicador += 1  # Incrementa o multiplicador

    # Exibe uma linha decorativa após a tabuada
    print('{}-=*=-{}'.format(cores['verde'], cores['limpa']) * 10)

# Mensagem de encerramento do programa
print('{}---FINALIZADO---{}'.format(cores['vermelho'], cores['limpa']))

