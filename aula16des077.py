cores = {'limpa': '\033[m', 'titulo': '\033[1;35m',
         'vermelho': '\033[31m', 'verde': '\033[32m', 'azul': '\033[34m'}

print('-=*=-' * 10)
print(f"{cores['titulo']}EXERCICIO 77{cores['limpa']}".center(60))
print('-=*=-' * 10)

palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar',
            'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')

for c in range(0, len(palavras)):
    print(f"\nNa palavra *{palavras[c]}*, temos as vogais: ", end='')
    for i in range(0, len(palavras[c])):
        if palavras[c][i] in 'aeiou':
            print(palavras[c][i], end='')