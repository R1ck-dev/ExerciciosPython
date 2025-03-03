cores = {'limpa': '\033[m', 'titulo': '\033[1;35m',
         'vermelho': '\033[31m', 'verde': '\033[32m', 'azul': '\033[34m'}

print('-=*=-' * 10)
print(f"{cores['titulo']}EXERCICIO 82{cores['limpa']}".center(60))
print('-=*=-' * 10)

valores = []

while True:
    num = int(input('Digite um valor: '))
    valores.append(num)
    continuar = input('Deseja continuar? (S/N): ').upper()
    if continuar != 'S':
        break
lista_par = []
lista_impar = []

for c in range(0, len(valores)):
    if valores[c] % 2 == 0:
        lista_par.append(valores[c])
    else:
        lista_impar.append((valores[c]))

print(f'Lista original: {valores}')
print(f'Lista de valores Par: {lista_par}')
print(f'Lista de valores Impar: {lista_impar}')