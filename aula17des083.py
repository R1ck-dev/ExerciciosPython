cores = {'limpa': '\033[m', 'titulo': '\033[1;35m',
         'vermelho': '\033[31m', 'verde': '\033[32m', 'azul': '\033[34m'}

print('-=*=-' * 10)
print(f"{cores['titulo']}EXERCICIO 83{cores['limpa']}".center(60))
print('-=*=-' * 10)

expressao = input("Insira uma expressão matemática: ")
aberto = expressao.count('(', 0, len(expressao))
fechado = expressao.count(')', 0, len(expressao))
primeiro_aberto = expressao.find('(')
primeiro_fechado = expressao.find(')')

if (aberto + fechado) % 2 == 0:
    if primeiro_fechado > primeiro_aberto:
        for pos, c in enumerate(range(0, len(expressao))):
            if expressao[c] == '(':
                if expressao[c+1] == ')':
                    print("Elementos Faltando!")
    else:
        print("Sua expressão está incorreta!")

else:
    print("Sua expressão está incorreta!")

