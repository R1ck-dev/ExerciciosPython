cores = {'limpa': '\033[m', 'titulo': '\033[1;35m',
         'vermelho': '\033[31m', 'verde': '\033[32m', 'azul': '\033[34m'}

print('-=*=-' * 10)
print(f"{cores['titulo']}EXERCICIO 89{cores['limpa']}".center(60))
print('-=*=-' * 10)

nnn = list()
nnn_final = list()

while True:
    nnn.append(input("Nome: "))
    nnn.append(float(input('Nota 1: ')))
    nnn.append(float(input('Nota 2: ')))
    nnn_final.append(nnn[:])
    continuar = str(input("Deseja Continuar? [S/N]: ")).strip().upper()
    if continuar != 'S':
        break
    nnn.clear()
print(f"{'No.':<10}{'Nome':^10}{'Média':>10}")
print('-'*35)
for i, l in enumerate(nnn_final):
    print(f'{i:<10}{l[0]:^10}{(l[1]+l[2])/2:>10}')
print('-'*35)

while True:
    mostra_n = int(input('Mostrar notas de quais alunos? (999 Interrompe): '))
    if mostra_n == 999:
        break
    print(f'Notas de {nnn_final[mostra_n][0]} são {nnn_final[mostra_n][1:]}')