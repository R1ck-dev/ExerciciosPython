cores = {'limpa': '\033[m', 'titulo': '\033[1;35m',
         'vermelho': '\033[31m', 'verde': '\033[32m', 'azul': '\033[34m'}

print('-=*=-' * 10)
print(' ' * 18, f"{cores['titulo']}EXERCICIO 75{cores['limpa']}")
print('-=*=-' * 10)

valores = (int(input()), int(input()), int(input()), int(input()))

print(valores)

cont9 = valores.count(9)
print(f"O valor 9 apareceu {cont9} vezes")

if 3 in valores:
    print(f"A posição do primeiro 3 na tupla é {valores.index(3)}")
else:
    print("O número 3 não apareceu!")

print("Os valores pares foram:", end=" ")
for c in range(0,4):
    if valores[c] % 2 == 0:
        print(valores[c], end=" ")