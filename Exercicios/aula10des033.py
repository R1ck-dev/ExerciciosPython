# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

# Solicita ao usuário três valores inteiros e armazena nas variáveis 'valor1', 'valor2' e 'valor3'
valor1 = int(input('Insira o valor 1: '))
valor2 = int(input('Insira o valor 2: '))
valor3 = int(input('Insira o valor 3: '))

maior = 0  # Inicializa a variável 'maior', que armazenará o maior valor

# Verifica qual número é o maior e ordena os valores em ordem decrescente
if valor1 > valor2 and valor1 > valor3:  # Se 'valor1' for o maior
    maior = valor1
    if valor2 > valor3:  # Verifica a ordem entre 'valor2' e 'valor3'
        print(f'{valor1} > {valor2} > {valor3}')
    else:
        print(f'{valor1} > {valor3} > {valor2}')
elif valor2 > valor1 and valor2 > valor3:  # Se 'valor2' for o maior
    maior = valor2
    if valor1 > valor3:  # Verifica a ordem entre 'valor1' e 'valor3'
        print(f'{valor2} > {valor1} > {valor3}')
    else:
        print(f'{valor2} > {valor3} > {valor1}')
elif valor3 > valor1 and valor3 > valor2:  # Se 'valor3' for o maior
    maior = valor3
    if valor1 > valor2:  # Verifica a ordem entre 'valor1' e 'valor2'
        print(f'{valor3} > {valor1} > {valor2}')
    else:
        print(f'{valor3} > {valor2} > {valor1}')
elif valor1 == valor2 and valor1 == valor3:  # Caso todos os valores sejam iguais
    print('Valores iguais!')
