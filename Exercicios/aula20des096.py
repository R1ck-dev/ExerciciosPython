# Dicionário com códigos ANSI para colorir a saída no terminal
cores = {'limpa': '\033[m', 'titulo': '\033[1;35m',
         'vermelho': '\033[31m', 'verde': '\033[32m', 'azul': '\033[34m'}

# Impressão do título formatado do exercício
print('-=*=-' * 10)
print(f"{cores['titulo']}EXERCICIO 96{cores['limpa']}".center(60))
print('-=*=-' * 10)

# Função que calcula a área do terreno
def area(a, b):
    # Calcula a área multiplicando a largura pela altura
    area_ = (a * b)
    # Exibe a área calculada
    print(f'A área de um terreno {a}x{b} é de {area_}m2')

# Solicita ao usuário que insira as dimensões do terreno
a = float(input("Largura (m): "))
b = float(input("Comprimento (m): "))

# Chama a função para calcular e exibir a área do terreno
area(a, b)
