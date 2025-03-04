# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

# Dicionário contendo códigos ANSI para formatação de cores no terminal
cores = {'limpa':'\033[m', 'titulo':'\033[1;35m',
         'vermelho':'\033[31m', 'verde':'\033[32m', 'azul':'\033[34m'}

# Exibição do cabeçalho do exercício formatado com cores
print('-=*=-'*10)
print(' '*18 , '{}EXERCICIO 55{}'.format(cores['titulo'], cores['limpa']))
print('-=*=-'*10)

# Solicita o peso da primeira pessoa e inicializa as variáveis de maior e menor peso com esse valor
maior = menor = float(input('Insira o peso da 1ª pessoa: '))

# Loop para ler os pesos das próximas 4 pessoas (totalizando 5)
for c in range(1, 5):
    peso = float(input(f'Insira o peso da {c+1}ª pessoa: '))  # Entrada do peso da pessoa

    # Atualiza a variável 'maior' caso o novo peso seja maior que o atual
    if peso > maior:
        maior = peso
    # Atualiza a variável 'menor' caso o novo peso seja menor que o atual
    elif peso < menor:
        menor = peso

# Exibição dos resultados com formatação de cores
print('{}{}{} foi o {}maior peso{}'.format(cores['titulo'], maior, cores['limpa'],
                                           cores['vermelho'], cores['limpa']))
print('{}{}{} foi o {}menor peso{}'.format(cores['titulo'], menor, cores['limpa'],
                                           cores['azul'], cores['limpa']))
