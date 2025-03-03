import math
num = int(input('Insira o valor de um ângulo qualquer: '))
radianos = math.radians(num)
print('O valor do seno de {} graus é igual a {:.3f}'.format(num, math.sin(radianos)))
print('O valor do cosseno de {} graus é igual a {:.3f}'.format(num, math.cos(radianos)))
print('O valor da tangente de {} graus é igual a {:.3f}'.format(num, math.tan(radianos)))