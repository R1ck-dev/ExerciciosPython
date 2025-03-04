# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

# Dicionário contendo códigos ANSI para colorir a saída no terminal
cores = {'limpa': '\033[m', 'titulo': '\033[1;35m',
         'vermelho': '\033[31m', 'verde': '\033[32m', 'azul': '\033[34m'}

# Impressão do título formatado do exercício
print('-=*=-' * 10)
print(f"{cores['titulo']}EXERCICIO 78{cores['limpa']}".center(60))
print('-=*=-' * 10)

# Criando uma lista com 5 valores fornecidos pelo usuário
valores = [int(input("Digite um valor: ")) for _ in range(5)]

# Inicializando as variáveis maior e menor com o primeiro valor da lista
maior = menor = valores[0]

# Inicializando as variáveis para armazenar as posições do maior e menor valor
posMaior = posMenor = 0

# Listas para armazenar todas as posições dos maiores e menores valores
listaMaiores = []
listaMenores = []

# Loop para encontrar o maior e o menor valor na lista
for pos, c in enumerate(range(0, len(valores))):
    if valores[c] > maior:
        maior = valores[c]
        posMaior = pos
    if valores[c] < menor:
        menor = valores[c]
        posMenor = pos

# Loop para armazenar todas as posições onde aparecem os maiores e menores valores
for pos, c in enumerate(range(0, len(valores))):
    if valores[c] == maior:
        listaMaiores.append(pos)
    if valores[c] == menor:
        listaMenores.append(pos)

# Exibindo os resultados
print(f'O maior valor foi {maior}, e as suas aparições foram nos índices {", ".join(map(str, listaMaiores))}')
print(f'O menor valor foi {menor}, e as suas aparições foram nos índices {", ".join(map(str, listaMenores))}')
