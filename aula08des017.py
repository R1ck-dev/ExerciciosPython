import math
c_oposto = float(input('Insira o valor do cateto oposto: '))
c_adjacente = float(input('Insira o valor do cateto adjacente: '))
hipo = math.sqrt(pow(c_oposto, 2) + pow(c_adjacente, 2))
print('O valor da hipotenusa referente aos catetos {} e {} é igual a {:.2f}'.format(c_oposto, c_adjacente, hipo))
