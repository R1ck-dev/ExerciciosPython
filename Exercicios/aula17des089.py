# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

# Dicionário contendo códigos ANSI para colorir a saída no terminal
cores = {'limpa': '\033[m', 'titulo': '\033[1;35m',
         'vermelho': '\033[31m', 'verde': '\033[32m', 'azul': '\033[34m'}

# Impressão do título formatado do exercício
print('-=*=-' * 10)
print(f"{cores['titulo']}EXERCICIO 89{cores['limpa']}".center(60))
print('-=*=-' * 10)

# Listas para armazenar os dados dos alunos
nnn = list()  # Lista temporária para armazenar nome e notas do aluno
nnn_final = list()  # Lista composta que armazenará todos os alunos e suas notas

# Loop para cadastrar os alunos e suas notas
while True:
    nnn.append(input("Nome: "))  # Lê o nome do aluno
    nnn.append(float(input('Nota 1: ')))  # Lê a primeira nota
    nnn.append(float(input('Nota 2: ')))  # Lê a segunda nota
    nnn_final.append(nnn[:])  # Adiciona uma cópia dos dados na lista final
    continuar = str(input("Deseja Continuar? [S/N]: ")).strip().upper()  # Pergunta se deseja continuar
    if continuar != 'S':  # Se a resposta não for 'S', o loop é encerrado
        break
    nnn.clear()  # Limpa a lista temporária para o próximo aluno

# Exibição do boletim com número, nome e média de cada aluno
print(f"{'No.':<10}{'Nome':^10}{'Média':>10}")
print('-' * 35)
for i, l in enumerate(nnn_final):
    print(f'{i:<10}{l[0]:^10}{(l[1]+l[2])/2:>10}')  # Calcula e exibe a média do aluno
print('-' * 35)

# Permite ao usuário visualizar as notas individuais dos alunos
while True:
    mostra_n = int(input('Mostrar notas de quais alunos? (999 Interrompe): '))  # Solicita um índice
    if mostra_n == 999:  # Se o usuário digitar 999, o loop é encerrado
        break
    print(f'Notas de {nnn_final[mostra_n][0]} são {nnn_final[mostra_n][1:]}')  # Exibe as notas do aluno escolhido
