# Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

# Dicionário com códigos ANSI para colorir a saída no terminal
cores = {'limpa': '\033[m', 'titulo': '\033[1;35m',
         'vermelho': '\033[31m', 'verde': '\033[32m', 'azul': '\033[34m'}

# Impressão do título formatado do exercício
print('-=*=-' * 10)
print(f"{cores['titulo']}EXERCICIO 102{cores['limpa']}".center(60))
print('-=*=-' * 10)

# Função fatorial que calcula o fatorial de um número
def fatorial(a, b):
    """
    Função para calcular o fatorial de qualquer valor
    :param a: valor a ser calculado o fatorial
    :param b: True ou False para indicar se o processo será mostrado ou não
    :return: o fatorial, (com o processo ou não)
    """
    f = 1  # Inicializa a variável fatorial com 1
    list_show = list()  # Lista para armazenar o processo de cálculo
    if b == False:  # Se 'b' for False, apenas retorna o fatorial final
        for c in range(1, a+1):  # Loop de 1 até o número 'a'
            f *= c  # Multiplica os números até 'a' para calcular o fatorial
        return f  # Retorna o resultado final do fatorial
    else:  # Se 'b' for True, mostra o processo de cálculo
        for c in range(1, a+1):  # Loop de 1 até o número 'a'
            f *= c  # Multiplica para calcular o fatorial
            list_show.append(c)  # Adiciona o número à lista do processo
        list_show.append(f)  # Adiciona o resultado final do fatorial
        # Converte os números e o resultado para string e retorna o processo de cálculo
        return ' * '.join(map(str, list_show[:-1])) + ' = ' + str(list_show[-1])


# Solicita ao usuário o valor para calcular o fatorial
valor_fato = int(input("Insira um valor: "))

# Pergunta ao usuário se ele quer ver o processo de cálculo
show_valor = str(input("Deseja ver o processo? [S/N]: ")).strip().upper()

# Valida a resposta do usuário para garantir que seja 'S' ou 'N'
while True:
    if show_valor not in 'SN':  # Verifica se a resposta está correta
        print("Erro! Utilize S ou N")  # Informa o erro
        show_valor = str(input("Deseja ver o processo? [S/N]: ")).strip().upper()  # Solicita novamente
    else:
        break  # Sai do loop quando a resposta for válida

# Exibe o resultado do fatorial com ou sem o processo, dependendo da escolha do usuário
if show_valor == 'S':  # Se o usuário escolheu 'S', mostra o processo
    print(fatorial(a=valor_fato, b=True))
else:  # Se o usuário escolheu 'N', apenas exibe o resultado final
    print(fatorial(a=valor_fato, b=False))

