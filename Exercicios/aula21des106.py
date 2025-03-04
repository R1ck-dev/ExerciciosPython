cores = {'limpa': '\033[m', 'titulo': '\033[1;35m',
         'vermelho': '\033[31m', 'verde': '\033[32m', 'azul': '\033[40m'}

print('-=*=-' * 10)
print(f"{cores['titulo']}EXERCICIO 106{cores['limpa']}".center(60))
print('-=*=-' * 10)

def ajuda(a):
    print(f"{cores['azul']}")
    help(a)
    print(f"{cores['limpa']}", end='')

def titulo(a):
    tam = len(a)
    print('~' * (tam+4))
    print(' ',a)
    print('~' * (tam+4), end='')


while True:
    print(end='' f"{cores['verde']}")
    titulo("Sistema de Ajuda PyHelp!")
    print(f"{cores['limpa']}")
    comando = input("Função ou Biblioteca: ").strip().lower()
    if comando == 'sair':
        print(end='' f"{cores['vermelho']}")
        titulo(f"Até Logo!")
        print(f"{cores['limpa']}", end='')
        break
    ajuda(comando)
