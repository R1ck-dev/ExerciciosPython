cores = {'limpa': '\033[m', 'titulo': '\033[1;35m',
         'vermelho': '\033[31m', 'verde': '\033[32m', 'azul': '\033[34m'}

print('-=*=-' * 10)
print(f"{cores['titulo']}EXERCICIO 86{cores['limpa']}".center(60))
print('-=*=-' * 10)

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_pares = 0

for c in range(0, 3):
    for i in range(0, 3):
        num = int(input(f"Insira o valor para [{c}, {i}]: "))
        matriz[c][i] = num
        if num % 2 == 0:
            soma_pares += num
soma_coluna3 = 0
for c in range(0, 3):
    soma_coluna3 += matriz[c][2]
maior = 0
for c in range(0, 3):
    if matriz[1][c] > maior:
        maior = matriz[1][c]
for c in range(0, 3):
    for i in range(0, 3):
        print(f'[{matriz[c][i]:^5}]', end='   ')
    print('\n')

print(f'A soma de todos os valores pares digitados: {soma_pares}')
print(f'A soma de todos os valores da terceira coluna: {soma_coluna3}')
print(f'O maior valor da segunda linha: {maior}')