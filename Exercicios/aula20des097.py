# Dicionário com códigos ANSI para colorir a saída no terminal
cores = {'limpa': '\033[m', 'titulo': '\033[1;35m',
         'vermelho': '\033[31m', 'verde': '\033[32m', 'azul': '\033[34m'}

# Impressão do título formatado do exercício
print('-=*=-' * 10)
print(f"{cores['titulo']}EXERCICIO 96{cores['limpa']}".center(60))
print('-=*=-' * 10)

# Função que recebe um texto e exibe uma mensagem com bordas adaptáveis ao tamanho do texto
def mensagem(txt):
    tam = len(txt) + 4  # O tamanho da linha da borda será o comprimento do texto + 4 (para espaços extras)
    print('-' * tam)  # Imprime a borda superior
    print(f'  {txt}')  # Imprime o texto no meio com espaçamento
    print('-' * tam)  # Imprime a borda inferior

# Chamadas da função com textos de exemplo
mensagem('Olá Mundo')
mensagem('Estudando Python')
