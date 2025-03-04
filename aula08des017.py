# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo
# retangulo, calcule e mostre o comprimento da hipotenusa

# Importa o módulo math para utilizar funções matemáticas, como sqrt (raiz quadrada) e pow (potenciação)
import math

# Solicita ao usuário que insira o valor do cateto oposto e armazena na variável 'c_oposto'
c_oposto = float(input('Insira o valor do cateto oposto: '))

# Solicita ao usuário que insira o valor do cateto adjacente e armazena na variável 'c_adjacente'
c_adjacente = float(input('Insira o valor do cateto adjacente: '))

# Calcula o valor da hipotenusa usando o Teorema de Pitágoras: h² = a² + b²
# Utiliza pow() para elevar ao quadrado e sqrt() para calcular a raiz quadrada
hipo = math.sqrt(pow(c_oposto, 2) + pow(c_adjacente, 2))

# Exibe o valor da hipotenusa formatado com duas casas decimais
print('O valor da hipotenusa referente aos catetos {} e {} é igual a {:.2f}'.format(c_oposto, c_adjacente, hipo))
