# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

# Solicita ao usuário a distância da viagem em quilômetros e armazena na variável 'distancia'
distancia = int(input('Insira a distância da viagem: '))

# Verifica se a distância é menor ou igual a 200 km
if distancia <= 200:
    # Se for até 200 km, o preço por km é R$ 0,50
    print('Preço da viagem (R$ 0.50 por KM): R$ {:.2f}'.format(0.5 * distancia))
else:
    # Para viagens acima de 200 km, o preço por km é R$ 0,45
    print('Preço da viagem (R$ 0.45 por KM): R$ {:.2f}'.format(0.45 * distancia))
