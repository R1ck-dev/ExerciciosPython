# Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

# Dicionário contendo códigos ANSI para colorir a saída no terminal
cores = {'limpa': '\033[m', 'titulo': '\033[1;35m',
         'vermelho': '\033[31m', 'verde': '\033[32m', 'azul': '\033[34m'}

# Impressão do título formatado do exercício
print('-=*=-' * 10)
print(f"{cores['titulo']}EXERCICIO 77{cores['limpa']}".center(60))
print('-=*=-' * 10)

# Tupla contendo várias palavras sem acentos
palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar',
            'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')

# Loop para percorrer cada palavra da tupla
for c in range(0, len(palavras)):
    print(f"\nNa palavra *{palavras[c]}*, temos as vogais: ", end='')

    # Loop para percorrer cada letra da palavra e verificar se é vogal
    for i in range(0, len(palavras[c])):
        if palavras[c][i] in 'aeiou':
            print(palavras[c][i], end='')  # Exibe as vogais da palavra
