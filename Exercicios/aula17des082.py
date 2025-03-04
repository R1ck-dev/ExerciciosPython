# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.

# Dicionário contendo códigos ANSI para colorir a saída no terminal
cores = {'limpa': '\033[m', 'titulo': '\033[1;35m',
         'vermelho': '\033[31m', 'verde': '\033[32m', 'azul': '\033[34m'}

# Impressão do título formatado do exercício
print('-=*=-' * 10)
print(f"{cores['titulo']}EXERCICIO 82{cores['limpa']}".center(60))
print('-=*=-' * 10)

# Lista principal que armazenará todos os números digitados
valores = []

# Loop para entrada de números até o usuário decidir parar
while True:
    num = int(input('Digite um valor: '))  # Lendo um número inteiro
    valores.append(num)  # Adiciona o número à lista principal

    # Pergunta se deseja continuar e converte a resposta para maiúscula
    continuar = input('Deseja continuar? (S/N): ').upper()
    if continuar != 'S':  # Se não for 'S', o loop é interrompido
        break

# Listas para armazenar os números pares e ímpares separadamente
lista_par = []
lista_impar = []

# Percorre a lista principal e separa os números em pares e ímpares
for c in range(0, len(valores)):
    if valores[c] % 2 == 0:
        lista_par.append(valores[c])  # Adiciona o número à lista de pares
    else:
        lista_impar.append(valores[c])  # Adiciona o número à lista de ímpares

# Exibição dos resultados
print(f'Lista original: {valores}')
print(f'Lista de valores Par: {lista_par}')
print(f'Lista de valores Impar: {lista_impar}')
