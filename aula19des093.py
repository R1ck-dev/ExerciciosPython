cores = {'limpa': '\033[m', 'titulo': '\033[1;35m',
         'vermelho': '\033[31m', 'verde': '\033[32m', 'azul': '\033[34m'}

print('-=*=-' * 10)
print(f"{cores['titulo']}EXERCICIO 93{cores['limpa']}".center(60))
print('-=*=-' * 10)

jogador = dict()
lista_gols = list()

jogador['nome'] = str(input("Nome do Jogador: "))
qtd_partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range(0, qtd_partidas):
    gol = int(input(f"Quantos gols na partida {c+1}? "))
    lista_gols.append(gol)
jogador['gols'] = lista_gols[:]
soma_gols = 0
for c in range(0, len(lista_gols)):
    soma_gols += lista_gols[c]
jogador['total'] = soma_gols
print('-=' *30)
print(jogador)
print('-=' *30)
for k, v in jogador.items():
    print(f'O campo {k} tem valor {v}')
print('-=' *30)
print(f'O jogador {jogador["nome"]} jogou {qtd_partidas} partidas.')
for i in range(0, len(lista_gols)):
    print(f'{"":>5} => Na partida {i+1}, fez {lista_gols[i]} gols.')
print(f'Foi um total de {jogador["total"]} gols')