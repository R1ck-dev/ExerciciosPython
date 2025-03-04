# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

# Dicionário contendo códigos ANSI para colorir a saída no terminal
cores = {'limpa': '\033[m', 'titulo': '\033[1;35m',
         'vermelho': '\033[31m', 'verde': '\033[32m', 'azul': '\033[34m'}

# Impressão do título formatado do exercício
print('-=*=-' * 10)
print(f"{cores['titulo']}EXERCICIO 83{cores['limpa']}".center(60))
print('-=*=-' * 10)

# Solicita ao usuário que insira uma expressão matemática
expressao = input("Insira uma expressão matemática: ")

# Conta quantos parênteses abertos e fechados existem na expressão
aberto = expressao.count('(', 0, len(expressao))
fechado = expressao.count(')', 0, len(expressao))

# Encontra as primeiras ocorrências de '(' e ')'
primeiro_aberto = expressao.find('(')
primeiro_fechado = expressao.find(')')

# Verifica se a quantidade de parênteses é par
if (aberto + fechado) % 2 == 0:
    # Verifica se o primeiro ')' aparece depois do primeiro '('
    if primeiro_fechado > primeiro_aberto:
        # Percorre a expressão para detectar erros
        for pos, c in enumerate(range(0, len(expressao))):
            if expressao[c] == '(':
                # Verifica se um '(' está imediatamente seguido de ')'
                if expressao[c+1] == ')':
                    print("Elementos Faltando!")
    else:
        print("Sua expressão está incorreta!")

else:
    print("Sua expressão está incorreta!")


