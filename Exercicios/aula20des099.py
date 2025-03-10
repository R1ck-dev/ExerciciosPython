# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

# Dicionário com códigos ANSI para colorir a saída no terminal
cores = {'limpa': '\033[m', 'titulo': '\033[1;35m',
         'vermelho': '\033[31m', 'verde': '\033[32m', 'azul': '\033[34m'}

# Impressão do título formatado do exercício
print('-=*=-' * 10)
print(f"{cores['titulo']}EXERCICIO 99{cores['limpa']}".center(60))
print('-=*=-' * 10)

# Função maior que recebe uma quantidade variável de parâmetros (valores inteiros)
def maior(*num):
    maior_ = num[0]  # Inicializa a variável maior com o primeiro valor
    # Laço para percorrer todos os valores passados como parâmetro
    for c in range(0, len(num)):
        # Se o valor atual for maior que o maior valor encontrado até agora
        if num[c] > maior_:
            maior_ = num[c]  # Atualiza a variável maior com o novo maior valor
    # Exibe os valores informados, a quantidade de valores e o maior valor
    print(f"Os valores informados foram {', '.join(map(str, num))}", end='')
    print(f"\nAo todo, {len(num)} valores foram informados")
    print(f'O maior valor é {maior_}')

# Função para imprimir uma linha de separação
def linhas():
    print('-'*30)  # Imprime uma linha de 30 traços

# Chamadas à função maior com diferentes números de parâmetros
linhas()
maior(5, 3, 5, 6, 1, 8, 9, 3)  # Primeira chamada com vários números
linhas()
maior(8, 5, 7, 3, 5, 6, 3, 4, 5)  # Segunda chamada com outros números
linhas()
maior(75, 3, 5, 33, 5, 5, 2, 4, 7, 4)  # Terceira chamada com outro conjunto de números
linhas()
