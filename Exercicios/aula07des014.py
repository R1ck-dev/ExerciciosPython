# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

# Solicita ao usuário que informe a temperatura em graus Celsius e armazena na variável 'c'
c = float(input('Informe a temperatura em Celsius: '))

# Converte a temperatura de Celsius para Fahrenheit usando a fórmula (C × 1.8) + 32
f = (c * 1.8) + 32

# Exibe a temperatura convertida para Fahrenheit, formatada com uma casa decimal
print('{} graus Celsius equivale a {:.1f} Fahrenheit'.format(c, f))
