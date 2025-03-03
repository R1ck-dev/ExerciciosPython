cores = {'limpa': '\033[m', 'titulo': '\033[1;35m',
         'vermelho': '\033[31m', 'verde': '\033[32m', 'azul': '\033[34m'}

print('-=*=-' * 10)
print(' ' * 18, f"{cores['titulo']}EXERCICIO 70{cores['limpa']}")
print('-=*=-' * 10)

valor = int(input('Qual valor você quer sacar: '))

nota50 = valor//50
nota50_resto = valor%50
nota20 = nota50_resto//20
nota20_resto = nota50_resto%20
nota10 = nota20_resto//10
nota10_resto = nota20_resto%10
nota1 = nota10_resto//1

print(f"{cores['titulo']}-=*=-{cores['limpa']}" * 10)
print(f"Quantidade de Notas 50: {cores['verde']}{nota50}{cores['limpa']}")
print(f"Quantidade de Notas 20: {cores['verde']}{nota20}{cores['limpa']}")
print(f"Quantidade de Notas 10: {cores['verde']}{nota10}{cores['limpa']}")
print(f"Quantidade de Notas 1: {cores['verde']}{nota1}{cores['limpa']}")
print(f"{cores['titulo']}-=*=-{cores['limpa']}" * 10)