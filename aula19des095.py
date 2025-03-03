cores = {'limpa': '\033[m', 'titulo': '\033[1;35m',
         'vermelho': '\033[31m', 'verde': '\033[32m', 'azul': '\033[34m'}

print('-=*=-' * 10)
print(f"{cores['titulo']}EXERCICIO 95{cores['limpa']}".center(60))
print('-=*=-' * 10)

jogador = dict()
list_gol = list()
list_jogadores = list()

while True:
    soma_gols = 0
    jogador['nome'] = str(input('Nome do Jogador: '))
    qtd_partidas = int(input(f"Quantas partidas {jogador['nome']} jogou? "))
    for c in range(0, qtd_partidas):
        gol = int(input(f"Quantos gols na partida {c+1}? "))
        list_gol.append(gol)
        soma_gols += gol
    jogador['gols'] = list_gol[:]
    jogador['total'] = soma_gols
    list_jogadores.append(jogador.copy())
    list_gol.clear()
    continuar = str(input("Quer continuar? [S/N]: ")).strip().upper()
    while continuar not in 'SN':
        print("ERRO! Responda com apenas S ou N.")
        continuar = str(input("Quer continuar? [S/N]: ")).strip().upper()
    if continuar == 'N':
        break
print('-=' * 35)
print(f'cod {"nome":>20} {"gols":>20} {"total":>20}')
print('--' * 35)
for c in range(0, len(list_jogadores)):
    print(f'[{c}] {list_jogadores[c]["nome"]:>20} {str(list_jogadores[c]["gols"]):>20} {list_jogadores[c]["total"]:>20}')
print('--' * 35)
while True:
    continuar_dados = int(input("Mostrar dados de qual jogador? (999 para parar) "))
    if continuar_dados < len(list_jogadores):
        print(f"-- Levantamento do jogador {list_jogadores[continuar_dados]['nome']}")
        for c in range(0, len(list_jogadores[continuar_dados]['gols'])):
            print(f'No jogo {c + 1} fez {list_jogadores[continuar_dados]["gols"][c]}')
    elif continuar_dados == 999:
        break
    else:
        print("ERRO! Insira o código de um jogador existente.")
