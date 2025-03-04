# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
#
# A) Quantas vezes apareceu o valor 9.
#
# B) Em que posição foi digitado o primeiro valor 3.
#
# C) Quais foram os números pares.

# Dicionário contendo códigos ANSI para colorir a saída no terminal
cores = {'limpa': '\033[m', 'titulo': '\033[1;35m',
         'vermelho': '\033[31m', 'verde': '\033[32m', 'azul': '\033[34m'}

# Impressão do título formatado do exercício
print('-=*=-' * 10)
print(' ' * 18, f"{cores['titulo']}EXERCICIO 75{cores['limpa']}")
print('-=*=-' * 10)

# Solicitação de quatro valores ao usuário e armazenamento em uma tupla
valores = (int(input()), int(input()), int(input()), int(input()))

# Exibição da tupla contendo os números digitados
print(valores)

# Contagem de quantas vezes o número 9 apareceu na tupla
cont9 = valores.count(9)
print(f"O valor 9 apareceu {cont9} vezes")

# Verificação se o número 3 está na tupla e exibição de sua primeira posição
if 3 in valores:
    print(f"A posição do primeiro 3 na tupla é {valores.index(3)}")
else:
    print("O número 3 não apareceu!")

# Exibição dos números pares presentes na tupla
print("Os valores pares foram:", end=" ")
for c in range(0, 4):
    if valores[c] % 2 == 0:
        print(valores[c], end=" ")
