cores = {'limpa': '\033[m', 'titulo': '\033[1;35m',
         'vermelho': '\033[31m', 'verde': '\033[32m', 'azul': '\033[34m'}

print('-=*=-' * 10)
print(f"{cores['titulo']}EXERCICIO 76{cores['limpa']}".center(60))
print('-=*=-' * 10)

itens_valores = (input(), float(input()),
                 input(), float(input()),
                 input(), float(input()),
                 input(), float(input()),
                 input(), float(input()))

print('======' * 10)
print("LISTAGEM DE PREÇOS".center(60))
print('======' * 10)

for c in range(0, len(itens_valores), 2):
    print(f"{itens_valores[c]:.<50}R${itens_valores[c+1]:.2f}")



