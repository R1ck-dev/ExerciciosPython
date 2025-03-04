# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

# Dicionário contendo códigos ANSI para colorir a saída no terminal
cores = {'limpa': '\033[m', 'titulo': '\033[1;35m',
         'vermelho': '\033[31m', 'verde': '\033[32m', 'azul': '\033[34m'}

# Impressão do título formatado do exercício
print('-=*=-' * 10)
print(f"{cores['titulo']}EXERCICIO 84{cores['limpa']}".center(60))
print('-=*=-' * 10)

# Lista temporária para armazenar nome e peso
original = list()
# Lista final para armazenar todos os cadastros
final = list()

# Loop para cadastrar pessoas
while True:
    original.append(str(input("Digite o nome: ")))  # Adiciona o nome
    original.append(int(input("Digite o peso: ")))  # Adiciona o peso

    # Adiciona a cópia da lista 'original' dentro da lista 'final'
    final.append(original[:])

    # Limpa a lista temporária para o próximo cadastro
    original.clear()

    # Pergunta se o usuário deseja continuar
    continuar = str(input("Deseja continuar? (S/N): ")).upper()
    if continuar != "S":
        break

# Inicializa as variáveis de maior e menor peso com o primeiro peso cadastrado
maior = menor = final[0][1]

# Listas para armazenar os mais pesados e mais leves
lista_pesadas = list()
lista_leves = list()

# Percorre a lista para encontrar o maior e o menor peso
for c in range(0, len(final)):
    if final[c][1] > maior:
        maior = final[c][1]
    if final[c][1] < menor:
        menor = final[c][1]

# Percorre a lista novamente para separar os nomes das pessoas mais pesadas e mais leves
for c in range(0, len(final)):
    if final[c][1] == maior:
        lista_pesadas.append(final[c][0])
    if final[c][1] == menor:
        lista_leves.append(final[c][0])

# Exibe os resultados
print(f'Quantidade de pessoas cadastradas: {len(final)}')
print(f'O maior peso registrado foi de {maior}KG. Peso de {lista_pesadas}')
print(f'O menor peso registrado foi de {menor}KG. Peso de {lista_leves}')



