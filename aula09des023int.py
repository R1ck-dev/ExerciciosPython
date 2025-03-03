valor = int(input('Insira um valor entre 0 e 9999: '))
unidade = valor%10
valor2 = valor//10
dezena = valor2%10
valor3 = valor2//10
centena = valor3%10
valor4 = valor3//10
milhar = valor4%10
print(f'Unidade: {unidade}')
print(f'Dezena: {dezena}')
print(f'Centena: {centena}')
print(f'Milhar: {milhar}')