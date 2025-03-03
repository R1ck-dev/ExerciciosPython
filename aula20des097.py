cores = {'limpa': '\033[m', 'titulo': '\033[1;35m',
         'vermelho': '\033[31m', 'verde': '\033[32m', 'azul': '\033[34m'}

print('-=*=-' * 10)
print(f"{cores['titulo']}EXERCICIO 96{cores['limpa']}".center(60))
print('-=*=-' * 10)

def mensagem(txt):
    tam = len(txt)+4
    print('-' * tam)
    print(f'  {txt}')
    print('-' * tam)

mensagem('Olá Mundo')
mensagem('Estudando Python')