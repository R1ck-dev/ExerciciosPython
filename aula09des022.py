nome = str(input('Insira um nome completo: '))
print('Nome completo maiusculo: {}'.format(nome.upper()))
print('Nome completo minusculo: {}'.format(nome.lower()))
print('Quantidade de letras (sem considerar espaços): {}'.format(len(nome.replace(' ', ''))))
nome_dividido = nome.split()
print('Letras no primeiro nome: {}'.format(len(nome_dividido[0][0:])))

