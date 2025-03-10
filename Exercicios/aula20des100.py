# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.

# Importa o módulo random para gerar números aleatórios
import random

# Dicionário com códigos ANSI para colorir a saída no terminal
cores = {'limpa': '\033[m', 'titulo': '\033[1;35m',
         'vermelho': '\033[31m', 'verde': '\033[32m', 'azul': '\033[34m'}

# Impressão do título formatado do exercício
print('-=*=-' * 10)
print(f"{cores['titulo']}EXERCICIO 100{cores['limpa']}".center(60))
print('-=*=-' * 10)

# Função que sorteia 5 números aleatórios e os coloca na lista 'numeros_final'
def sortear():
    for c in range(0, 5):
        # Sorteia um índice aleatório entre 0 e o tamanho da lista 'numeros'
        valor_s = random.randint(0, len(numeros)-1)
        # Adiciona o número sorteado na lista 'numeros_final'
        numeros_final.append(numeros[valor_s])
    # Exibe os números sorteados
    print(f'Numeros sorteados: {numeros_final}')

# Função que calcula e exibe a soma dos números pares na lista 'numeros_final'
def somar():
    soma = 0  # Inicializa a variável soma
    # Laço para percorrer todos os números na lista 'numeros_final'
    for c in range(0, len(numeros_final)):
        # Verifica se o número é par
        if numeros_final[c] % 2 == 0:
            soma += numeros_final[c]  # Adiciona o número par à soma
    # Exibe a soma dos números pares
    print(f'Soma total dos números pares: {soma}')

# Lista vazia onde os números serão armazenados
numeros = list()
# Lista onde os números sorteados serão armazenados
numeros_final = list()

# Laço que permite ao usuário inserir valores para a lista 'numeros'
while True:
    valor = int(input("Insira valores para a lista: "))
    if valor == 999:  # Condição para parar a inserção
        break
    # Adiciona o valor informado pelo usuário na lista 'numeros'
    numeros.append(valor)

# Exibe a lista de números inseridos
print(numeros)
# Chama a função 'sortear' para sortear 5 números
sortear()
# Chama a função 'somar' para somar os números pares sorteados
somar()


