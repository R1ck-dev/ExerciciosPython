# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

# Solicita ao usuário que informe a largura da parede em metros e armazena na variável 'largura'
largura = float(input('Informe a largura da parede: '))

# Solicita ao usuário que informe a altura da parede em metros e armazena na variável 'altura'
altura = float(input('Informe a altura da parede: '))

# Calcula a área da parede multiplicando largura por altura
area = largura * altura

# Calcula a quantidade de tinta necessária, considerando que 1 litro cobre 2m²
qtd_tinta = area / 2

# Exibe a quantidade de tinta necessária para pintar a parede
print(f'Será necessário {qtd_tinta} litros de tinta para pintar toda a parede')
