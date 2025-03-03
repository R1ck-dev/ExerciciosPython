cores = {'limpa': '\033[m', 'titulo': '\033[1;35m',
         'vermelho': '\033[31m', 'verde': '\033[32m', 'azul': '\033[34m'}

print('-=*=-' * 10)
print(f"{cores['titulo']}EXERCICIO 85{cores['limpa']}".center(60))
print('-=*=-' * 10)

valores = [[], []]

for c in range(0, 7):
    num = int(input('Insira um valor: '))
    if num % 2 == 0:
        par = num
        valores[0].append(num)
    else:
        impar = num
        valores[1].append(num)
valores[0].sort()
valores[1].sort()
print(valores)