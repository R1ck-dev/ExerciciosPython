# Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:
#
# considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

# Dicionário de cores para formatação do texto no terminal
cores = {'limpa': '\033[m', 'titulo': '\033[1;35m',
         'vermelho': '\033[31m', 'verde': '\033[32m', 'azul': '\033[34m'}

# Exibição do título do exercício
print('-=*=-' * 10)
print(' ' * 18, f"{cores['titulo']}EXERCICIO 70{cores['limpa']}")
print('-=*=-' * 10)

# Solicita o valor a ser sacado
valor = int(input('Qual valor você quer sacar: '))

# Cálculo da quantidade de notas de cada valor
nota50 = valor // 50  # Calcula quantas notas de R$50 são necessárias
nota50_resto = valor % 50  # Calcula o restante após as notas de R$50

nota20 = nota50_resto // 20  # Calcula quantas notas de R$20 são necessárias
nota20_resto = nota50_resto % 20  # Calcula o restante após as notas de R$20

nota10 = nota20_resto // 10  # Calcula quantas notas de R$10 são necessárias
nota10_resto = nota20_resto % 10  # Calcula o restante após as notas de R$10

nota1 = nota10_resto // 1  # Calcula quantas notas de R$1 são necessárias

# Exibição dos resultados
print(f"{cores['titulo']}-=*=-{cores['limpa']}" * 10)
print(f"Quantidade de Notas 50: {cores['verde']}{nota50}{cores['limpa']}")
print(f"Quantidade de Notas 20: {cores['verde']}{nota20}{cores['limpa']}")
print(f"Quantidade de Notas 10: {cores['verde']}{nota10}{cores['limpa']}")
print(f"Quantidade de Notas 1: {cores['verde']}{nota1}{cores['limpa']}")
print(f"{cores['titulo']}-=*=-{cores['limpa']}" * 10)
