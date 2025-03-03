cores = {'limpa': '\033[m', 'titulo': '\033[1;35m',
         'vermelho': '\033[31m', 'verde': '\033[32m', 'azul': '\033[34m'}

print('-=*=-' * 10)
print(f"{cores['titulo']}EXERCICIO 86{cores['limpa']}".center(60))
print('-=*=-' * 10)

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for c in range(0, 3):
    for i in range(0, 3):
        num = int(input(f"Insira o valor para [{c}, {i}]: "))
        matriz[c][i] = num
for c in range(0, 3):
    for i in range(0, 3):
        print(f'[{matriz[c][i]:^5}]', end='   ')
    print('\n')