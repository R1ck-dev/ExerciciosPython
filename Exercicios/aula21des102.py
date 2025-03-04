cores = {'limpa': '\033[m', 'titulo': '\033[1;35m',
         'vermelho': '\033[31m', 'verde': '\033[32m', 'azul': '\033[34m'}

print('-=*=-' * 10)
print(f"{cores['titulo']}EXERCICIO 102{cores['limpa']}".center(60))
print('-=*=-' * 10)

def fatorial(a, b):
    """
    Função para calcular o fatorial de qualquer valor
    :param a: valor a ser calculado o fatorial
    :param b: True or False para indicar se o processo será mostrado ou não
    :return: o fatorial, (com o processo ou não)
    """
    f = 1
    list_show = list()
    if b == False:
        for c in range(1, a+1):
            f *= c
        return f
    else:
        for c in range(1, a+1):
            f *= c
            list_show.append(c)
        list_show.append(f)
        return ' * '.join(map(str, list_show[:-1])) + ' = ' + str(list_show[-1])


valor_fato = int(input("Insira um valor: "))
show_valor = str(input("Deseja ver o processo? [S/N]: ")).strip().upper()
while True:
    if show_valor not in 'SN':
        print("Erro! Utilize S ou N")
        show_valor = str(input("Deseja ver o processo? [S/N]: ")).strip().upper()
    else:
        break
if show_valor == 'S':
    print(fatorial(a=valor_fato, b=True))
else:
    print(fatorial(a=valor_fato, b=False))
