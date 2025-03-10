# Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. Importante: use cores.

# Dicionário com códigos ANSI para colorir a saída no terminal
cores = {'limpa': '\033[m', 'titulo': '\033[1;35m',
         'vermelho': '\033[31m', 'verde': '\033[32m', 'azul': '\033[34m'}

# Impressão do título formatado do exercício
print('-=*=-' * 10)
print(f"{cores['titulo']}EXERCICIO 106{cores['limpa']}".center(60))
print('-=*=-' * 10)

# Função que exibe o help com as cores
def ajuda(a):
    print(f"{cores['azul']}")  # Cor azul para o help
    help(a)  # Chama o help do Python
    print(f"{cores['limpa']}", end='')  # Restaura a cor normal

# Função para exibir o título com barras
def titulo(a):
    tam = len(a)
    print('~' * (tam + 4))  # Imprime barras ao redor do título
    print(' ', a)
    print('~' * (tam + 4), end='')

# Loop principal para interação com o usuário
while True:
    print(f"{cores['verde']}", end='')  # Cor verde para o título
    titulo("Sistema de Ajuda PyHelp!")  # Exibe o título
    print(f"{cores['limpa']}")  # Restaura a cor normal
    comando = input("Função ou Biblioteca (ou 'FIM' para sair): ").strip().lower()  # Solicita o comando
    
    if comando == 'fim':  # Se o usuário digitar 'FIM', o programa se encerra
        print(f"{cores['vermelho']}", end='')  # Cor vermelha para a despedida
        titulo("Até Logo!")  # Exibe a mensagem de despedida
        print(f"{cores['limpa']}")  # Restaura a cor normal
        break  # Encerra o loop e o programa
    
    ajuda(comando)  # Exibe o help do comando solicitado

