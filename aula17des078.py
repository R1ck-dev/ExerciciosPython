cores = {'limpa': '\033[m', 'titulo': '\033[1;35m',
         'vermelho': '\033[31m', 'verde': '\033[32m', 'azul': '\033[34m'}

print('-=*=-' * 10)
print(f"{cores['titulo']}EXERCICIO 78{cores['limpa']}".center(60))
print('-=*=-' * 10)

valores = [int(input("Digite um valor: ")) for _ in range(5)]

maior = menor = valores[0]
posMaior = posMenor = 0
listaMaiores = []
listaMenores = []

for pos, c in enumerate(range(0, len(valores))):
    if valores[c] > maior:
        maior = valores[c]
        posMaior = pos
    if valores[c] < menor:
        menor = valores[c]
        posMenor = pos
for pos, c in enumerate(range(0, len(valores))):
    if valores[c] == maior:
        listaMaiores.append(pos)
    if valores[c] == menor:
        listaMenores.append(pos)

print(f'O maior valor foi {maior}, e as suas aparições foram nos indices {", ".join(map(str, listaMaiores))}')
print(f'O menor valor foi {menor}, e as suas aparições foram nos indices {", ".join(map(str, listaMenores))}')

