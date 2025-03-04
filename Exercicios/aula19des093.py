# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

# Dicionário contendo códigos ANSI para colorir a saída no terminal
cores = {'limpa': '\033[m', 'titulo': '\033[1;35m',
         'vermelho': '\033[31m', 'verde': '\033[32m', 'azul': '\033[34m'}

# Impressão do título formatado do exercício
print('-=*=-' * 10)
print(f"{cores['titulo']}EXERCICIO 93{cores['limpa']}".center(60))
print('-=*=-' * 10)

# Dicionário para armazenar os dados do jogador
jogador = dict()
# Lista para armazenar a quantidade de gols em cada partida
lista_gols = list()

# Entrada do nome do jogador
jogador['nome'] = str(input("Nome do Jogador: "))

# Entrada do número de partidas jogadas
qtd_partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

# Loop para registrar os gols em cada partida
for c in range(0, qtd_partidas):
    gol = int(input(f"Quantos gols na partida {c + 1}? "))
    lista_gols.append(gol)  # Adiciona os gols à lista

# Armazena a lista de gols dentro do dicionário do jogador
jogador['gols'] = lista_gols[:]

# Calcula o total de gols somando os valores da lista
soma_gols = 0
for c in range(0, len(lista_gols)):
    soma_gols += lista_gols[c]

# Adiciona o total de gols ao dicionário do jogador
jogador['total'] = soma_gols

# Exibe o dicionário completo
print('-=' * 30)
print(jogador)
print('-=' * 30)

# Exibe os dados de forma detalhada
for k, v in jogador.items():
    print(f'O campo {k} tem valor {v}')
print('-=' * 30)

# Exibe o desempenho do jogador
print(f'O jogador {jogador["nome"]} jogou {qtd_partidas} partidas.')
for i in range(0, len(lista_gols)):
    print(f'{"":>5} => Na partida {i + 1}, fez {lista_gols[i]} gols.')

# Exibe o total de gols marcados no campeonato
print(f'Foi um total de {jogador["total"]} gols')
