cores = {'limpa': '\033[m', 'titulo': '\033[1;35m',
         'vermelho': '\033[31m', 'verde': '\033[32m', 'azul': '\033[34m'}

print('-=*=-' * 10)
print(f"{cores['titulo']}EXERCICIO 80{cores['limpa']}".center(60))
print('-=*=-' * 10)

valores = []
for c in range(0, 5):
    indice = 0
    num = int(input("Digite um valor: "))
    for i in range(0, len(valores)):
        if num > valores[i]:
            indice += 1
    valores.insert(indice, num)
    print(f'Valor {num} foi adicionado na posição {indice} da lista')
print(valores)
