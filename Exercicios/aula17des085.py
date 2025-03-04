# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

# Dicionário contendo códigos ANSI para colorir a saída no terminal
cores = {'limpa': '\033[m', 'titulo': '\033[1;35m',
         'vermelho': '\033[31m', 'verde': '\033[32m', 'azul': '\033[34m'}

# Impressão do título formatado do exercício
print('-=*=-' * 10)
print(f"{cores['titulo']}EXERCICIO 85{cores['limpa']}".center(60))
print('-=*=-' * 10)

# Lista com duas sublistas:
# valores[0] para armazenar os números pares e valores[1] para os ímpares
valores = [[], []]

# Laço para coletar 7 números do usuário
for c in range(0, 7):
    num = int(input('Insira um valor: '))  # Recebe o número do usuário

    # Verifica se o número é par ou ímpar e adiciona na respectiva sublista
    if num % 2 == 0:
        valores[0].append(num)  # Adiciona à lista de pares
    else:
        valores[1].append(num)  # Adiciona à lista de ímpares

# Ordena os valores dentro de cada sublista
valores[0].sort()
valores[1].sort()

# Exibe as listas organizadas
print(f'Lista de valores pares: {valores[0]}')
print(f'Lista de valores ímpares: {valores[1]}')
