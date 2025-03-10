# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada:                                                                                                                                                                            
# a) de 1 até 10, de 1 em 1                                                                                                                                              
# b) de 10 até 0, de 2 em 2                                                                                                                                            
# c) uma contagem personalizada

import time

# Dicionário com códigos ANSI para colorir a saída no terminal
cores = {'limpa': '\033[m', 'titulo': '\033[1;35m',
         'vermelho': '\033[31m', 'verde': '\033[32m', 'azul': '\033[34m'}

# Impressão do título formatado do exercício
print('-=*=-' * 10)
print(f"{cores['titulo']}EXERCICIO 98{cores['limpa']}".center(60))
print('-=*=-' * 10)

# Função contador que recebe início, fim e passo para realizar a contagem
def contador(comeco, fim, passo):
    c = comeco  # Variável auxiliar c, que é o contador
    # Se a contagem for crescente (início menor que fim)
    if comeco < fim:
        # Laço para contagem crescente, de 'comeco' até 'fim' com 'passo'
        for c in range(comeco, fim+1, passo):
            print(comeco, end=' ')  # Imprime o valor de 'comeco'
            comeco += passo  # Atualiza 'comeco' somando o passo
            time.sleep(0.5)  # Pausa de 0.5 segundos entre cada número
        print()  # Quebra a linha após a contagem
    # Se a contagem for decrescente (início maior que fim)
    else:
        # Laço para contagem decrescente, de 'comeco' até 'fim' com '-passo'
        for c in range(comeco, fim-1, -passo):
            print(comeco, end=' ')  # Imprime o valor de 'comeco'
            comeco -= passo  # Atualiza 'comeco' subtraindo o passo
            time.sleep(0.5)  # Pausa de 0.5 segundos entre cada número
        print()  # Quebra a linha após a contagem

# Função para imprimir uma linha de separação
def linhas():
    print('-'*30)  # Imprime uma linha de 30 traços

# Contagem de 1 até 10, de 1 em 1
linhas()
print('Contador de 1 a 10:')
contador(1, 10, 1)  # Chama a função contador com 1, 10 e passo 1
linhas()

# Contagem de 10 até 0, de 2 em 2
print('Contador de 10 a 0 (passo 2):')
contador(10, 0, 2)  # Chama a função contador com 10, 0 e passo 2
linhas()

# Contagem personalizada pelo usuário
print('Contador Personalizado: ')
contador(comeco=int(input("Começo: ")), fim=int(input("Fim: ")), passo=abs(int(input("Passo: "))))  # Chama a função contador com os valores fornecidos pelo usuário

# Linha de fechamento
linhas()
