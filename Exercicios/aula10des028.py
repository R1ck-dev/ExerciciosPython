# Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

# Importa a biblioteca 'random' para gerar um número aleatório
import random

# Gera um número inteiro aleatório entre 0 e 5 e armazena na variável 'valor'
valor = random.randint(0, 5)

# Solicita ao usuário que digite um número entre 0 e 5 e armazena na variável 'jogada'
jogada = int(input("Escolha um valor de 0 a 5: "))

# Compara a escolha do usuário com o número gerado pelo computador
if jogada == valor:
    print('Venceu!')  # Se os valores forem iguais, o usuário vence
else:
    print('Perdeu!')  # Caso contrário, o usuário perde

# Exibe uma mensagem final indicando o fim do programa
print("\n---FIM---")

