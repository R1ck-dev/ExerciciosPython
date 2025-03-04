# Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

# Dicionário de cores ANSI para personalizar a saída do terminal
cores = {'limpa': '\033[m', 'titulo': '\033[1;35m',
         'vermelho': '\033[31m', 'verde': '\033[32m', 'azul': '\033[34m'}

# Impressão do título do programa
print('-=*=-' * 10)
print(f"{cores['titulo']}EXERCICIO 95{cores['limpa']}".center(60))
print('-=*=-' * 10)

# Declaração das estruturas de dados
jogador = dict()  # Dicionário que armazenará os dados de cada jogador
list_gol = list()  # Lista temporária para armazenar os gols de cada jogador
list_jogadores = list()  # Lista que armazenará todos os jogadores cadastrados

# Loop para cadastro de jogadores
while True:
    soma_gols = 0  # Variável para armazenar a soma dos gols do jogador
    jogador['nome'] = str(input('Nome do Jogador: '))  # Nome do jogador
    qtd_partidas = int(input(f"Quantas partidas {jogador['nome']} jogou? "))  # Número de partidas jogadas

    # Coleta do número de gols em cada partida
    for c in range(0, qtd_partidas):
        gol = int(input(f"Quantos gols na partida {c + 1}? "))  # Número de gols em uma partida
        list_gol.append(gol)  # Adiciona à lista de gols
        soma_gols += gol  # Atualiza o total de gols

    # Adiciona as informações no dicionário do jogador
    jogador['gols'] = list_gol[:]  # Clona a lista de gols
    jogador['total'] = soma_gols  # Armazena o total de gols no campeonato
    list_jogadores.append(jogador.copy())  # Adiciona o jogador à lista de jogadores
    list_gol.clear()  # Limpa a lista temporária de gols para o próximo jogador

    # Pergunta se deseja continuar cadastrando jogadores
    continuar = str(input("Quer continuar? [S/N]: ")).strip().upper()
    while continuar not in 'SN':  # Validação da entrada
        print("ERRO! Responda com apenas S ou N.")
        continuar = str(input("Quer continuar? [S/N]: ")).strip().upper()

    if continuar == 'N':  # Se o usuário optar por não continuar, o loop se encerra
        break

# Exibição do cabeçalho da tabela de jogadores
print('-=' * 35)
print(f'cod {"nome":>20} {"gols":>20} {"total":>20}')
print('--' * 35)

# Exibição dos dados de cada jogador
for c in range(0, len(list_jogadores)):
    print(
        f'[{c}] {list_jogadores[c]["nome"]:>20} {str(list_jogadores[c]["gols"]):>20} {list_jogadores[c]["total"]:>20}')
print('--' * 35)

# Loop para exibir detalhes do aproveitamento de jogadores individuais
while True:
    continuar_dados = int(input("Mostrar dados de qual jogador? (999 para parar) "))

    # Se o código inserido for válido, exibe os detalhes do jogador
    if continuar_dados < len(list_jogadores):
        print(f"-- Levantamento do jogador {list_jogadores[continuar_dados]['nome']}")
        for c in range(0, len(list_jogadores[continuar_dados]['gols'])):
            print(f'No jogo {c + 1} fez {list_jogadores[continuar_dados]["gols"][c]} gols.')

    # Se o usuário digitar 999, o programa encerra essa funcionalidade
    elif continuar_dados == 999:
        break

    # Se o código for inválido, exibe uma mensagem de erro
    else:
        print("ERRO! Insira o código de um jogador existente.")

