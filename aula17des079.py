cores = {'limpa': '\033[m', 'titulo': '\033[1;35m',
         'vermelho': '\033[31m', 'verde': '\033[32m', 'azul': '\033[34m'}

print('-=*=-' * 10)
print(f"{cores['titulo']}EXERCICIO 79{cores['limpa']}".center(60))
print('-=*=-' * 10)

valores = []
continuar = ''
while True:
    num = int(input("Digite um valor: "))

    if num in valores:
        print("Valor já existente!")
    else:
        valores.append(num)

    continuar = input("Deseja continuar? (S/N): ").upper()
    if continuar != 'S':
        break
valores.sort()
print(valores)