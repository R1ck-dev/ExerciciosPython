cores = {'limpa': '\033[m', 'titulo': '\033[1;35m',
         'vermelho': '\033[31m', 'verde': '\033[32m', 'azul': '\033[34m'}

print('-=*=-' * 10)
print(f"{cores['titulo']}EXERCICIO 105{cores['limpa']}".center(60))
print('-=*=-' * 10)

def notas(*num,  b=False):
    resp = dict()
    qtd_notas = len(num)
    maior = menor = num[0]
    soma = 0
    for c in range(0, len(num)):
        soma += num[c]
        if num[c] > maior:
            maior = num[c]
        elif num[c] < menor:
            menor = num[c]
    resp['Total'] = qtd_notas
    resp['Maior'] = maior
    resp['Menor'] = menor
    resp['Média'] = soma/qtd_notas
    if b:
        if resp['Média'] >= 8:
            resp['Situação'] = 'Ótima'
        elif 8 > resp['Média'] >= 6:
            resp['Situação'] = 'Razoável'
        else:
            resp['Situação'] = 'Ruim'
    return resp

notas_list = list()
while True:
    valor = input("Insira a nota: ")
    while not valor.isnumeric():
        print("ERRO! Insira um valor numérico!")
        valor = float(input("Insira a nota: "))
    notas_list.append(float(valor))
    continuar = input("Deseja Continuar? [S/N]: ").strip().lower()
    if continuar == 'n':
        break
sit = str(input("Deseja mostrar a situação da classe? [S/N]: ")).strip().lower()
if sit not in 'sn':
    print("ERRO! Responda com S ou N")
    sit = str(input("Deseja mostrar a situação da classe? [S/N]: ")).strip().lower()
if sit == 's':
    print(notas(*notas_list, b=True)) #O * serve para desempacotar a lista e enviar os argumentos individualmente
else:
    print(notas(*notas_list))
