cores = {'limpa': '\033[m', 'titulo': '\033[1;35m',
         'vermelho': '\033[31m', 'verde': '\033[32m', 'azul': '\033[34m'}

print('-=*=-' * 10)
print(' ' * 18, f"{cores['titulo']}EXERCICIO 70{cores['limpa']}")
print('-=*=-' * 10)

total_compra = produtos_mais1000 = 0

nome_menorproduto = ''
menor = float('inf')

while True:
    nome_produto = input('Insira o nome do produto: ')
    while True:
        try:
            valor = int(input(f"Insira o preço do item {cores['titulo']}[{nome_produto}]{cores['limpa']}: "))
            break
        except ValueError:
            print(f"{cores['vermelho']}[ENTRADA ERRADA]{cores['limpa']} Insira o preço do item "
                              f"{cores['titulo']}[{nome_produto}]{cores['limpa']}")
    total_compra += valor
    if valor > 1000:
        produtos_mais1000 += 1
    if valor < menor:
        menor = valor
        nome_menorproduto = nome_produto
    s_n = input('Deseja Continuar? [s/n]: ').lower()
    while s_n not in ['s', 'n']:
        s_n = input(f"{cores['vermelho']}[ENTRADA ERRADA]{cores['limpa']} Deseja Continuar? [s/n]: ").lower()
    if s_n == 'n':
        break
print(f"----{cores['verde']}FIM DO PROGRAMA{cores['limpa']}----")
print(f"O total da compra foi {cores['titulo']}R$ {total_compra}{cores['limpa']}.")
print(f"Temos {cores['titulo']}{produtos_mais1000}{cores['limpa']} itens custando mais de R$ 1000.00")
print(f"O produto mais barato foi {cores['titulo']}{nome_menorproduto}{cores['limpa']}, com o preço de"
      f" {cores['titulo']}R$ {menor}{cores['limpa']}.")



