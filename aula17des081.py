cores = {'limpa': '\033[m', 'titulo': '\033[1;35m',
         'vermelho': '\033[31m', 'verde': '\033[32m', 'azul': '\033[34m'}

print('-=*=-' * 10)
print(f"{cores['titulo']}EXERCICIO 81{cores['limpa']}".center(60))
print('-=*=-' * 10)

valores = []
qtd_valores = 0
valor_cinco = 0
while True:
    num = int(input("Digite um valor: "))
    if num == 5:
        valor_cinco = 1
    valores.append(num)
    qtd_valores += 1
    continuar = input("Deseja continuar? (S/N): ").upper()
    if continuar != 'S':
        break
print(f'A quantidade de valores digitados foi: {qtd_valores}')
valores.sort(reverse=True)
print(f'Os valores digitados foram {valores}')
if valor_cinco == 1:
    print('O valor cinco está presente na lista!')
else:
    print('O valor cinco não está presenta na lista!')