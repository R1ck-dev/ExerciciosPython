distancia = int(input('Insira a distância da viagem: '))
if distancia <= 200:
    print('Preço da viagem (R$ 0.50 por KM): R$ {:.2f}'.format(0.5*distancia))
else:
    print('Preço da viagem (R$ 0.45 por KM): R$ {:.2f}'.format(0.45 * distancia))