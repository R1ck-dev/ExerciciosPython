cores = {'limpa': '\033[m', 'titulo': '\033[1;35m',
         'vermelho': '\033[31m', 'verde': '\033[32m', 'azul': '\033[34m'}

print('-=*=-' * 10)
print(f"{cores['titulo']}EXERCICIO 104{cores['limpa']}".center(60))
print('-=*=-' * 10)

def leiaint(a):
    while not a.isnumeric():
        print(f"{cores['vermelho']}ERRO! Digite um número: {cores['limpa']}", end='')
        a = input()
    return a

valor = leiaint(input("Digite um número: "))
print(f"Você acabou de digitar o número {valor}")
