import time

cores = {'limpa': '\033[m', 'titulo': '\033[1;35m',
         'vermelho': '\033[31m', 'verde': '\033[32m', 'azul': '\033[34m'}

print('-=*=-' * 10)
print(f"{cores['titulo']}EXERCICIO 98{cores['limpa']}".center(60))
print('-=*=-' * 10)

def contador(comeco, fim, passo):
    c = comeco
    if comeco < fim:
        for c in range(comeco, fim+passo, passo):
            print(comeco, end=' ')
            comeco += passo
            time.sleep(0.5)
        print()
    else:
        for c in range(comeco, fim-passo, (passo*-1)):
            print(comeco, end=' ')
            comeco -= passo
            time.sleep(0.5)
        print()

def linhas():
    print('-'*30)


linhas()
print('Contador de 1 a 10:')
contador(1, 10, 1)
linhas()
print('Contador de 10 a 0 (passo 2):')
contador(10, 0, 2)
linhas()
print('Contador Personalizado: ')
contador(comeco=int(input("Começo: ")), fim=int(input("Fim: ")), passo=abs(int(input("Passo: "))))
linhas()