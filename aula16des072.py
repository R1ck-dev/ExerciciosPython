cores = {'limpa': '\033[m', 'titulo': '\033[1;35m',
         'vermelho': '\033[31m', 'verde': '\033[32m', 'azul': '\033[34m'}

print('-=*=-' * 10)
print(' ' * 18, f"{cores['titulo']}EXERCICIO 72{cores['limpa']}")
print('-=*=-' * 10)

valores = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez",
           "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")

while True:
    entrada = int(input("Insira o valor [0 a 20] que deseja ver por extenso: "))
    if entrada < 0 or entrada > 20:
        print(f"{cores['vermelho']}Valor fora de alcance, tente Novamente!{cores['limpa']}")
    else:
        break

print(f"\n{cores['azul']}{valores[entrada]}{cores['limpa']}")