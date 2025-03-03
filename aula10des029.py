vel = int(input('Insira a velocidade do carro: '))
if vel > 80:
    print('\nUltrapossou o limite de velocidade!')
    multa = float(7*(vel-80))
    print('O valor da multa é de R$ {:.2f}'.format(multa))
else:
    print('Dentro do limite de velocidade!')