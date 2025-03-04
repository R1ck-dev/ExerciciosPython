cores = {'limpa': '\033[m', 'titulo': '\033[1;35m',
         'vermelho': '\033[31m', 'verde': '\033[32m', 'azul': '\033[34m'}

print('-=*=-' * 10)
print(f"{cores['titulo']}EXERCICIO 103{cores['limpa']}".center(60))
print('-=*=-' * 10)

def ficha(a='<desconhecido>', b=0):
    return f'O jogador {a} fez {b} gol(s) no campeonato.'


nome = str(input("Nome do Jogador: ")).strip()
gols = input("Quantidade de Gols: ").strip()

gols = int(gols) if gols.isdigit() else 0

if nome == '':
    print(ficha(b=gols))
else:
    print(ficha(a=nome, b=gols))
