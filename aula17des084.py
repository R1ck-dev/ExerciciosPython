cores = {'limpa': '\033[m', 'titulo': '\033[1;35m',
         'vermelho': '\033[31m', 'verde': '\033[32m', 'azul': '\033[34m'}

print('-=*=-' * 10)
print(f"{cores['titulo']}EXERCICIO 84{cores['limpa']}".center(60))
print('-=*=-' * 10)

original = list()
final = list()

while True:
    original.append(str(input("Digite o nome: ")))
    original.append(int(input("Digite o peso: ")))
    final.append(original[:])
    original.clear()
    continuar = str(input("Deseja continuar? (S/N): ")).upper()
    if continuar != "S":
        break

maior = menor = final[0][1]
lista_pesadas = list()
lista_leves = list()

for c in range(0, len(final)):
    if final[c][1] > maior:
        maior = final[c][1]
    if final[c][1] < menor:
        menor = final[c][1]
for c in range(0, len(final)):
    if final[c][1] == maior:
        lista_pesadas.append(final[c][0])
    if final[c][1] == menor:
        lista_leves.append(final[c][0])

print(f'Quantidade de pessoas cadastradas: {len(final)}')
print(f'O maior peso registrado foi de {maior}KG. Peso de {lista_pesadas}')
print(f'O menor peso registrado foi de {menor}KG. Peso de {lista_leves}')


