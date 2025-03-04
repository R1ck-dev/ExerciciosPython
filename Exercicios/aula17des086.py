# Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.

# Dicionário contendo códigos ANSI para colorir a saída no terminal
cores = {'limpa': '\033[m', 'titulo': '\033[1;35m',
         'vermelho': '\033[31m', 'verde': '\033[32m', 'azul': '\033[34m'}

# Impressão do título formatado do exercício
print('-=*=-' * 10)
print(f"{cores['titulo']}EXERCICIO 86{cores['limpa']}".center(60))
print('-=*=-' * 10)

# Inicializa uma matriz 3x3 preenchida com zeros
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# Preenchendo a matriz com valores digitados pelo usuário
for c in range(0, 3):  # Percorre as linhas
    for i in range(0, 3):  # Percorre as colunas
        num = int(input(f"Insira o valor para [{c}, {i}]: "))  # Lê o valor
        matriz[c][i] = num  # Armazena na posição correta

# Exibição da matriz formatada
for c in range(0, 3):  # Percorre as linhas
    for i in range(0, 3):  # Percorre as colunas
        print(f'[{matriz[c][i]:^5}]', end='   ')  # Exibe o valor formatado com espaçamento
    print('\n')  # Quebra de linha após cada linha da matriz
