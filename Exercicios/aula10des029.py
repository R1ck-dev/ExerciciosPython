# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

# Solicita ao usuário que insira a velocidade do carro e armazena na variável 'vel'
vel = int(input('Insira a velocidade do carro: '))

# Verifica se a velocidade ultrapassou 80 km/h
if vel > 80:
    print('\nUltrapassou o limite de velocidade!')  # Exibe mensagem de infração

    # Calcula o valor da multa (R$7,00 para cada km acima do limite)
    multa = float(7 * (vel - 80))

    # Exibe o valor da multa com duas casas decimais
    print('O valor da multa é de R$ {:.2f}'.format(multa))
else:
    print('Dentro do limite de velocidade!')  # Mensagem para quem não foi multado
