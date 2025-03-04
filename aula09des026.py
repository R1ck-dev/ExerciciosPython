# Faça um programa que leia uma frase pelo teclado e mostre:
# - Quantas vezes aparece a letra A
# - Em que posição ela aparece a primeira vez
# - Em que posição ela aparece a ultima vez

# Solicita ao usuário que insira uma frase e armazena na variável 'frase'
frase = input('Insira uma frase: ')

# Conta quantas vezes a letra 'a' aparece na frase (case-sensitive)
print('Quantas vezes aparece a letra a: {}'.format(frase.count('a')))

# Encontra a posição da primeira ocorrência da letra 'a' na frase
# O método find() retorna o índice da primeira aparição ou -1 se não existir
print('[a] aparece pela primeira vez na posição: {}'.format(frase.find('a')))

# Encontra a posição da última ocorrência da letra 'a' na frase
# O método rfind() busca a letra a partir do final da string
print('[a] aparece pela última vez na posição: {}'.format(frase.rfind('a')))
