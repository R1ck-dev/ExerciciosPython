#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento

# Solicita ao usuário que informe o salário inicial e armazena na variável 'salario'
salario = float(input('Insira aqui o salário inicial: '))

# Calcula o novo salário aplicando um aumento de 15% (multiplicando por 0.15 e somando ao valor original)
salario_final = salario + (salario * 0.15)

# Exibe o novo salário com o aumento, formatado com duas casas decimais
print('O salário final com o acréscimo de 15% é de R$ {:.2f}'.format(salario_final))
