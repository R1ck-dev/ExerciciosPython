salario = float(input('Insira o seu salário: '))
if salario > 1250:
    print('Aumento de 10%!')
    print('Novo salário: R$ {:.2f}'.format((0.1*salario)+salario))
else:
    print('Aumento de 15%!')
    print('Novo salário: R$ {:.2f}'.format((0.15 * salario) + salario))