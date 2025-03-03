import random
valor = random.randint(0, 5)
jogada = int(input("Escolha um valor de 0 a 5: "))
if jogada == valor:
    print('Venceu!')
else:
    print('Perdeu!')
print("\n---FIM---")
