# Aprimore o desafio anterior, mostrando no final.
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

# Dicionário contendo códigos ANSI para colorir a saída no terminal
cores = {'limpa': '\033[m', 'titulo': '\033[1;35m',
         'vermelho': '\033[31m', 'verde': '\033[32m', 'azul': '\033[34m'}

# Impressão do título formatado do exercício
print('-=*=-' * 10)
print(f"{cores['titulo']}EXERCICIO 86{cores['limpa']}".center(60))
print('-=*=-' * 10)

# Inicializa uma matriz 3x3 preenchida com zeros
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_pares = 0  # Variável para armazenar a soma dos valores pares

# Preenchendo a matriz com valores digitados pelo usuário
for c in range(0, 3):  # Percorre as linhas
    for i in range(0, 3):  # Percorre as colunas
        num = int(input(f"Insira o valor para [{c}, {i}]: "))  # Lê o valor
        matriz[c][i] = num  # Armazena na posição correta
        if num % 2 == 0:  # Verifica se o número é par
            soma_pares += num  # Soma os valores pares

# Cálculo da soma dos valores da terceira coluna
soma_coluna3 = 0
for c in range(0, 3):  # Percorre as linhas
    soma_coluna3 += matriz[c][2]  # Soma os valores da terceira coluna

# Determinar o maior valor da segunda linha
maior = 0
for c in range(0, 3):  # Percorre as colunas da segunda linha
    if matriz[1][c] > maior:
        maior = matriz[1][c]

# Exibição da matriz formatada
for c in range(0, 3):  # Percorre as linhas
    for i in range(0, 3):  # Percorre as colunas
        print(f'[{matriz[c][i]:^5}]', end='   ')  # Exibe o valor formatado
    print('\n')  # Quebra de linha após cada linha da matriz

# Exibição dos resultados solicitados
print(f'A soma de todos os valores pares digitados: {soma_pares}')
print(f'A soma de todos os valores da terceira coluna: {soma_coluna3}')
print(f'O maior valor da segunda linha: {maior}')
