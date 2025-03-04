# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
#
# A) quantas pessoas tem mais de 18 anos.
#
# B) quantos homens foram cadastrados.
#
# C) quantas mulheres tem menos de 20 anos.

# Dicionário de cores para formatação do texto no terminal
cores = {'limpa': '\033[m', 'titulo': '\033[1;35m',
         'vermelho': '\033[31m', 'verde': '\033[32m', 'azul': '\033[34m'}

# Exibição do título do exercício
print('-=*=-' * 10)
print(' ' * 18, f"{cores['titulo']}EXERCICIO 69{cores['limpa']}")
print('-=*=-' * 10)

# Variáveis para contagem das condições pedidas no exercício
cont_mais18 = 0  # Contador de pessoas com mais de 18 anos
qtd_homens = 0  # Contador de homens cadastrados
qtd_mulheres20 = 0  # Contador de mulheres com menos de 20 anos

# Loop principal do programa
while True:
    # Validação da idade (garante que o usuário insira um número inteiro)
    while True:
        try:
            idade = int(input('Insira a idade: '))
            break  # Sai do loop se a entrada for válida
        except ValueError:
            print('Entrada inválida! Insira um número válido para a idade.')

    # Verifica se a pessoa tem mais de 18 anos
    if idade > 18:
        cont_mais18 += 1

    # Validação do sexo (garante que a entrada seja 'm' ou 'f')
    sexo = input('Insira o sexo [f/m]: ').lower()
    while sexo not in ['m', 'f']:
        sexo = input('Entrada inválida! Insira o sexo [f/m]: ').lower()

    # Contagem de homens cadastrados
    if sexo == 'm':
        qtd_homens += 1
    # Contagem de mulheres com menos de 20 anos
    elif sexo == 'f' and idade < 20:
        qtd_mulheres20 += 1

    # Validação para continuar o programa (garante que a entrada seja 's' ou 'n')
    continuar = input('Deseja continuar [s/n]: ').lower()
    while continuar not in ['s', 'n']:
        continuar = input('Entrada inválida! Deseja continuar [s/n]: ').lower()

    # Exibição da separação visual no terminal
    print(f"{cores['titulo']}-=*=-{cores['limpa']}" * 10)

    # Se o usuário não quiser continuar, o loop é encerrado
    if continuar == 'n':
        break

# Exibição dos resultados finais
print('Programa Finalizado!')
print(f'Quantidade de Homens = {qtd_homens}')
print(f'Homens maiores de 18 anos = {cont_mais18}')
print(f'Mulheres com menos de 20 anos = {qtd_mulheres20}')
