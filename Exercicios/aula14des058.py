# Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

# Importa a biblioteca 'random' para gerar números aleatórios
import random

# Dicionário contendo códigos ANSI para formatação de cores no terminal
cores = {'limpa':'\033[m', 'titulo':'\033[1;35m',
         'vermelho':'\033[31m', 'verde':'\033[32m', 'azul':'\033[34m'}

# Exibição do cabeçalho do exercício formatado com cores
print('-=*=-'*10)
print(' '*18 , '{}EXERCICIO 58{}'.format(cores['titulo'], cores['limpa']))
print('-=*=-'*10)

# O computador escolhe um número aleatório entre 0 e 10
valor = random.randint(0, 10)

# O jogador faz a primeira tentativa
jogada = int(input("Escolha um valor de 0 a 10: "))
tentativas = 1  # Contador de tentativas

# Se o palpite estiver errado, entra no loop até acertar
if jogada != valor:
    while jogada != valor:
        print('Tentativa {}errada!{}'.format(cores['vermelho'], cores['limpa']))  # Feedback de erro
        tentativas += 1  # Incrementa o número de tentativas
        # Solicita um novo palpite
        jogada = int(input("{}[TENTE DE NOVO]{} Escolha um valor de 0 a 10: ".format(cores['titulo'], cores['limpa'])))

    # Quando o jogador acerta, exibe a mensagem de sucesso
    print('Tentativa {}correta!{}'.format(cores['azul'], cores['limpa']))
    print('Foram necessárias {}{}{} tentativas.'.format(cores['verde'], tentativas, cores['limpa']))
else:
    # Caso o jogador acerte de primeira
    print('Tentativa {}correta!{}'.format(cores['azul'], cores['limpa']))
    print('Foi necessário apenas {}1{} tentativa.'.format(cores['verde'], cores['limpa']))
