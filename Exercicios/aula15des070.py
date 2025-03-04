# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
#
# A) qual é o total gasto na compra.
#
# B) quantos produtos custam mais de R$1000.
#
# C) qual é o nome do produto mais barato.

# Dicionário de cores para formatação do texto no terminal
cores = {'limpa': '\033[m', 'titulo': '\033[1;35m',
         'vermelho': '\033[31m', 'verde': '\033[32m', 'azul': '\033[34m'}

# Exibição do título do exercício
print('-=*=-' * 10)
print(' ' * 18, f"{cores['titulo']}EXERCICIO 70{cores['limpa']}")
print('-=*=-' * 10)

# Variáveis para armazenar os dados da compra
total_compra = 0  # Armazena o total gasto
produtos_mais1000 = 0  # Conta quantos produtos custam mais de R$1000
nome_menorproduto = ''  # Armazena o nome do produto mais barato
menor = float('inf')  # Inicializa com um valor infinito para comparar preços

# Loop principal do programa
while True:
    # Solicita o nome do produto
    nome_produto = input('Insira o nome do produto: ')

    # Validação do preço (garante que a entrada seja um número inteiro)
    while True:
        try:
            valor = int(input(f"Insira o preço do item {cores['titulo']}[{nome_produto}]{cores['limpa']}: "))
            break  # Sai do loop se a entrada for válida
        except ValueError:
            print(f"{cores['vermelho']}[ENTRADA ERRADA]{cores['limpa']} Insira o preço do item "
                  f"{cores['titulo']}[{nome_produto}]{cores['limpa']}")

    # Soma o preço ao total da compra
    total_compra += valor

    # Verifica se o produto custa mais de R$1000
    if valor > 1000:
        produtos_mais1000 += 1

    # Verifica qual é o produto mais barato
    if valor < menor:
        menor = valor
        nome_menorproduto = nome_produto

    # Pergunta ao usuário se deseja continuar cadastrando produtos
    s_n = input('Deseja Continuar? [s/n]: ').lower()
    while s_n not in ['s', 'n']:
        s_n = input(f"{cores['vermelho']}[ENTRADA ERRADA]{cores['limpa']} Deseja Continuar? [s/n]: ").lower()

    # Se a resposta for 'n', o loop é encerrado
    if s_n == 'n':
        break

# Exibição dos resultados finais
print(f"----{cores['verde']}FIM DO PROGRAMA{cores['limpa']}----")
print(f"O total da compra foi {cores['titulo']}R$ {total_compra}{cores['limpa']}.")
print(f"Temos {cores['titulo']}{produtos_mais1000}{cores['limpa']} itens custando mais de R$ 1000.00")
print(f"O produto mais barato foi {cores['titulo']}{nome_menorproduto}{cores['limpa']}, com o preço de"
      f" {cores['titulo']}R$ {menor}{cores['limpa']}.")



