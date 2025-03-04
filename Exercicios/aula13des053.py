# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:

# Dicionário contendo códigos ANSI para formatação de cores no terminal
cores = {'limpa':'\033[m', 'titulo':'\033[1;35m',
         'vermelho':'\033[31m', 'verde':'\033[32m', 'azul':'\033[34m'}

# Exibição do cabeçalho do exercício formatado com cores
print('-=*=-'*10)
print(' '*18 , '{}EXERCICIO 53{}'.format(cores['titulo'], cores['limpa']))
print('-=*=-'*10)

# Solicita ao usuário uma frase e remove os espaços para a verificação do palíndromo
frase = input('Insira a frase a ser analisada: ').replace(' ', '')

# Variável para armazenar a frase invertida
frase_contrario = ''

# Laço que percorre a frase de trás para frente
for c in range(len(frase) - 1, -1, -1):
    frase_contrario += frase[c]  # Constrói a string invertida caractere por caractere

# Compara a frase original (sem espaços) com sua versão invertida
if frase == frase_contrario:
    print('{}São Palíndromos!{}'.format(cores['verde'], cores['limpa']))
else:
    print('{}Não são Palíndromos!{}'.format(cores['vermelho'], cores['limpa']))

# Exibição de verificações auxiliares
print('-=*=-'*10)
print(frase)  # Mostra a frase sem espaços
print(frase_contrario)  # Mostra a frase invertida
