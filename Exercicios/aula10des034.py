# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

# Solicita ao usuário o valor do salário e armazena na variável 'salario'
salario = float(input('Insira o seu salário: '))

# Verifica se o salário é maior que R$ 1250,00
if salario > 1250:
    print('Aumento de 10%!')  # Exibe a mensagem de aumento de 10%
    print('Novo salário: R$ {:.2f}'.format((0.1 * salario) + salario))  # Calcula e exibe o novo salário
else:
    print('Aumento de 15%!')  # Exibe a mensagem de aumento de 15%
    print('Novo salário: R$ {:.2f}'.format((0.15 * salario) + salario))  # Calcula e exibe o novo salário
