valor1 = int(input('Insira o valor 1: '))
valor2 = int(input('Insira o valor 2: '))
valor3 = int(input('Insira o valor 3: '))
maior = 0

if valor1 > valor2 and valor1 > valor3:
    maior = valor1
    if valor2 > valor3:
        print(f'{valor1} > {valor2} > {valor3}')
    else:
        print(f'{valor1} > {valor3} > {valor2}')
elif valor2 > valor1 and valor2 > valor3:
    maior = valor2
    if valor1 > valor3:
        print(f'{valor2} > {valor1} > {valor3}')
    else:
        print(f'{valor2} > {valor3} > {valor1}')
elif valor3 > valor1 and valor3 > valor2:
    maior = valor3
    if valor1 > valor2:
        print(f'{valor3} > {valor1} > {valor2}')
    else:
        print(f'{valor3} > {valor2} > {valor1}')
elif valor1 == valor2 and valor1 == valor3:
    print('Valores iguais!')