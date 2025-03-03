nome = str(input('Insira o nome de uma cidade: '))
primeira_palavra = nome.split()
s_n = 'Santo' in primeira_palavra[0][0:]
print(s_n)