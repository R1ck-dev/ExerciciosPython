frase = input('Insira uma frase: ')
print('Quantas vezes aparece a letra a: {}'.format(frase.count('a')))
print('[a] aparece pela primeira vez na posição: {}'.format(frase.find('a')))
print('[a] aparece pela última vez na posição: {}'.format(frase.rfind('a')))