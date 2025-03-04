# Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

cores = {'limpa': '\033[m', 'titulo': '\033[1;35m',
         'vermelho': '\033[31m', 'verde': '\033[32m', 'azul': '\033[34m'}

print('-=*=-' * 10)
print(f"{cores['titulo']}EXERCICIO 96{cores['limpa']}".center(60))
print('-=*=-' * 10)

def area(a, b):
    area_ = (a * b)
    print(f'A área de um terreno {a}x{b} é de {area_}m2')


a = float(input("Largura (m): "))
b = float(input("Comprimento (m): "))
area(a, b)