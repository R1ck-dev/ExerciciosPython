# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

# Solicita ao usuário que insira a primeira nota e a converte para ponto flutuante (float)
num1 = float(input('Digite a primeira nota: '))

# Solicita ao usuário que insira a segunda nota e a converte para ponto flutuante (float)
num2 = float(input('Digite a segunda nota: '))

# Calcula a média das duas notas
media = (num1 + num2) / 2

# Exibe a média do aluno, formatada com uma casa decimal
print('A média do aluno é {:.1f}'.format(media))
