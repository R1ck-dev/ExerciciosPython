# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

# Dicionário contendo códigos ANSI para colorir a saída no terminal
cores = {'limpa': '\033[m', 'titulo': '\033[1;35m',
         'vermelho': '\033[31m', 'verde': '\033[32m', 'azul': '\033[34m'}

# Impressão do título formatado do exercício
print('-=*=-' * 10)
print(f"{cores['titulo']}EXERCICIO 81{cores['limpa']}".center(60))
print('-=*=-' * 10)

# Lista para armazenar os valores digitados
valores = []
qtd_valores = 0  # Contador de quantidade de valores digitados
valor_cinco = 0  # Variável para indicar se o número 5 foi digitado

# Loop para entrada de números até o usuário decidir parar
while True:
    num = int(input("Digite um valor: "))  # Lendo um número inteiro

    if num == 5:
        valor_cinco = 1  # Sinaliza que o número 5 foi digitado

    valores.append(num)  # Adiciona o número à lista
    qtd_valores += 1  # Incrementa a quantidade de valores

    continuar = input("Deseja continuar? (S/N): ").upper()  # Pergunta se deseja continuar
    if continuar != 'S':  # Se não for 'S', sai do loop
        break

# Exibe a quantidade de números digitados
print(f'A quantidade de valores digitados foi: {qtd_valores}')

# Ordena a lista em ordem decrescente
valores.sort(reverse=True)

# Exibe a lista ordenada de forma decrescente
print(f'Os valores digitados foram {valores}')

# Verifica se o número 5 está na lista e exibe a mensagem correspondente
if valor_cinco == 1:
    print('O valor cinco está presente na lista!')
else:
    print('O valor cinco não está presente na lista!')
