# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

# Importa o módulo math para utilizar funções matemáticas, como seno, cosseno e tangente
import math

# Solicita ao usuário que insira um ângulo em graus e armazena na variável 'num'
num = int(input('Insira o valor de um ângulo qualquer: '))

# Converte o ângulo de graus para radianos, pois as funções trigonométricas do Python utilizam radianos
radianos = math.radians(num)

# Calcula e exibe o valor do seno do ângulo, formatado com três casas decimais
print('O valor do seno de {} graus é igual a {:.3f}'.format(num, math.sin(radianos)))

# Calcula e exibe o valor do cosseno do ângulo, formatado com três casas decimais
print('O valor do cosseno de {} graus é igual a {:.3f}'.format(num, math.cos(radianos)))

# Calcula e exibe o valor da tangente do ângulo, formatado com três casas decimais
print('O valor da tangente de {} graus é igual a {:.3f}'.format(num, math.tan(radianos)))
