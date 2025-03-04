import random

cores = {'limpa': '\033[m', 'titulo': '\033[1;35m',
         'vermelho': '\033[31m', 'verde': '\033[32m', 'azul': '\033[34m'}

print('-=*=-' * 10)
print(f"{cores['titulo']}EXERCICIO 100{cores['limpa']}".center(60))
print('-=*=-' * 10)

def sortear():
    for c in range(0, 5):
        valor_s = random.randint(0, len(numeros)-1)
        numeros_final.append(numeros[valor_s])
    print(f'Numeros sorteados: {numeros_final}')

def somar():
    soma = 0
    for c in range(0, len(numeros_final)):
        if numeros_final[c] % 2 == 0:
            soma += numeros_final[c]
    print(f'Soma total do numeros pares: {soma}')


numeros = list()
numeros_final = list()
while True:
    valor = int(input("Insira valores para a lista: "))
    if valor == 999:
        break
    numeros.append(valor)

print(numeros)
sortear()
somar()

