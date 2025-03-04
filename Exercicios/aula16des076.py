# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.

# Dicionário contendo códigos ANSI para colorir a saída no terminal
cores = {'limpa': '\033[m', 'titulo': '\033[1;35m',
         'vermelho': '\033[31m', 'verde': '\033[32m', 'azul': '\033[34m'}

# Impressão do título formatado do exercício
print('-=*=-' * 10)
print(f"{cores['titulo']}EXERCICIO 76{cores['limpa']}".center(60))
print('-=*=-' * 10)

# Armazenamento dos nomes dos produtos e seus respectivos preços em uma tupla
itens_valores = (input(), float(input()),  # Primeiro produto e preço
                 input(), float(input()),  # Segundo produto e preço
                 input(), float(input()),  # Terceiro produto e preço
                 input(), float(input()),  # Quarto produto e preço
                 input(), float(input()))  # Quinto produto e preço

# Impressão do cabeçalho da listagem de preços
print('======' * 10)
print("LISTAGEM DE PREÇOS".center(60))
print('======' * 10)

# Exibição dos produtos e seus preços de forma tabular
for c in range(0, len(itens_valores), 2):
    print(f"{itens_valores[c]:.<50}R${itens_valores[c+1]:.2f}")




