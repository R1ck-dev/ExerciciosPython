# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

# Solicita ao usuário que insira um número entre 0 e 9999
valor = int(input('Insira um valor entre 0 e 9999: '))

# Obtém o dígito da unidade (último número)
unidade = valor % 10

# Remove o último dígito e obtém o valor restante
valor2 = valor // 10

# Obtém o dígito da dezena
dezena = valor2 % 10

# Remove o dígito da dezena e obtém o valor restante
valor3 = valor2 // 10

# Obtém o dígito da centena
centena = valor3 % 10

# Remove o dígito da centena e obtém o valor restante
valor4 = valor3 // 10

# Obtém o dígito do milhar
milhar = valor4 % 10

# Exibe os dígitos separados
print(f'Unidade: {unidade}')
print(f'Dezena: {dezena}')
print(f'Centena: {centena}')
print(f'Milhar: {milhar}')
