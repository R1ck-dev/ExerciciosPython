cores = {'limpa': '\033[m', 'titulo': '\033[1;35m',
         'vermelho': '\033[31m', 'verde': '\033[32m', 'azul': '\033[34m'}

print('-=*=-' * 10)
print(f"{cores['titulo']}EXERCICIO 99{cores['limpa']}".center(60))
print('-=*=-' * 10)

def maior(*num):
    maior_ = num[0]
    for c in range(0, len(num)):
        if num[c] > maior_:
            maior_ = num[c]
    print(f"Os valores informados foram {", ".join(map(str, num))}", end='')
    print(f"\nAo todo, {len(num)} valores foram informados")
    print(f'O maior valor é {maior_}')

def linhas():
    print('-'*30)


linhas()
maior(5,3,5,6,1,8,9,3)
linhas()
maior(8,5,7,3,5,6,3,4,5)
linhas()
maior(75,3,5,33,5,5,2,4,7,4)
linhas()