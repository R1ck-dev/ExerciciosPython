#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada

# Solicita ao usuário que insira um número inteiro e armazena na variável 'num'
num = int(input('Digite um valor: '))

# Exibe o dobro do número digitado
print(f'O dobro de [{num}] é {num*2}')

# Exibe o triplo do número digitado
print(f'O triplo de [{num}] é {num*3}')

# Calcula a raiz quadrada do número e exibe o resultado formatado com duas casas decimais
print('A raiz quadrada de [{}] é {:.2f}'.format(num, (num**(1/2))))
