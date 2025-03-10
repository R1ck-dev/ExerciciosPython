# Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.

# Dicionário com códigos ANSI para colorir a saída no terminal
cores = {'limpa': '\033[m', 'titulo': '\033[1;35m',
         'vermelho': '\033[31m', 'verde': '\033[32m', 'azul': '\033[34m'}

# Impressão do título formatado do exercício
print('-=*=-' * 10)
print(f"{cores['titulo']}EXERCICIO 103{cores['limpa']}".center(60))
print('-=*=-' * 10)

# Função ficha que recebe dois parâmetros opcionais: nome do jogador e número de gols
def ficha(a='<desconhecido>', b=0):
    """
    Função para exibir as informações do jogador
    :param a: Nome do jogador (opcional, padrão '<desconhecido>')
    :param b: Quantidade de gols do jogador (opcional, padrão 0)
    :return: String formatada com as informações do jogador
    """
    return f'O jogador {a} fez {b} gol(s) no campeonato.'

# Solicita o nome do jogador e a quantidade de gols
nome = str(input("Nome do Jogador: ")).strip()  # Recebe o nome e remove espaços extras
gols = input("Quantidade de Gols: ").strip()  # Recebe a quantidade de gols como string e remove espaços

# Verifica se a quantidade de gols é um número válido (se é um número inteiro)
gols = int(gols) if gols.isdigit() else 0  # Se for um número válido, converte para int, caso contrário, usa 0

# Se o nome estiver vazio, utiliza o valor padrão '<desconhecido>'
if nome == '':  
    print(ficha(b=gols))  # Chama a função ficha com o nome padrão e os gols informados
else:
    print(ficha(a=nome, b=gols))  # Chama a função ficha com o nome e gols informados

