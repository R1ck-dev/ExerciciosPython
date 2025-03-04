# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

# Solicita ao usuário os comprimentos das três retas
a = int(input('Valor da reta A: '))
b = int(input('Valor da reta B: '))
c = int(input('Valor da reta C: '))

# Verifica a condição de existência de um triângulo:
# A soma de dois lados deve ser sempre maior que o terceiro lado
if (a + b) > c and (a + c) > b and (b + c) > a:
    print('Podem formar um triângulo!')  # Se a condição for verdadeira, exibe a mensagem positiva
else:
    print('Não podem formar um triângulo!')  # Caso contrário, informa que não é possível formar um triângulo
