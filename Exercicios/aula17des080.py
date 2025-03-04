# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

# Dicionário contendo códigos ANSI para colorir a saída no terminal
cores = {'limpa': '\033[m', 'titulo': '\033[1;35m',
         'vermelho': '\033[31m', 'verde': '\033[32m', 'azul': '\033[34m'}

# Impressão do título formatado do exercício
print('-=*=-' * 10)
print(f"{cores['titulo']}EXERCICIO 80{cores['limpa']}".center(60))
print('-=*=-' * 10)

# Criando uma lista vazia para armazenar os valores ordenados
valores = []

# Loop para receber 5 valores numéricos do usuário
for c in range(0, 5):
    indice = 0  # Inicializa o índice onde o número será inserido
    num = int(input("Digite um valor: "))  # Lendo um número inteiro do usuário

    # Percorre a lista já ordenada para encontrar a posição correta
    for i in range(0, len(valores)):
        if num > valores[i]:  # Se o número for maior que o da posição atual
            indice += 1  # Avança o índice de inserção

    # Insere o número na posição correta para manter a lista ordenada
    valores.insert(indice, num)
    print(f'Valor {num} foi adicionado na posição {indice} da lista')

# Exibindo a lista ordenada no final
print(valores)

