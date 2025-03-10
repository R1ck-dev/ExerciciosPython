# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:

# Dicionário com códigos ANSI para colorir a saída no terminal
cores = {'limpa': '\033[m', 'titulo': '\033[1;35m',
         'vermelho': '\033[31m', 'verde': '\033[32m', 'azul': '\033[34m'}

# Impressão do título formatado do exercício
print('-=*=-' * 10)
print(f"{cores['titulo']}EXERCICIO 105{cores['limpa']}".center(60))
print('-=*=-' * 10)

# Função notas que calcula as informações sobre as notas dos alunos
def notas(*num, b=False):
    """
    Função para calcular as informações das notas fornecidas.
    :param num: As notas dos alunos.
    :param b: (opcional) Se True, calcula e retorna a situação da classe.
    :return: Um dicionário com Total de notas, Maior, Menor e Média, e opcionalmente, a Situação.
    """
    resp = dict()  # Dicionário para armazenar os resultados
    qtd_notas = len(num)  # Quantidade de notas fornecidas
    maior = menor = num[0]  # Inicializando maior e menor com a primeira nota
    soma = 0  # Inicializando soma das notas
    for c in range(0, len(num)):  # Percorre todas as notas
        soma += num[c]  # Soma todas as notas
        if num[c] > maior:  # Verifica se a nota atual é maior
            maior = num[c]
        elif num[c] < menor:  # Verifica se a nota atual é menor
            menor = num[c]
    
    # Preenche o dicionário com as informações calculadas
    resp['Total'] = qtd_notas
    resp['Maior'] = maior
    resp['Menor'] = menor
    resp['Média'] = soma / qtd_notas  # Calcula a média

    # Se b for True, calcula a situação da classe
    if b:
        if resp['Média'] >= 8:
            resp['Situação'] = 'Ótima'
        elif 8 > resp['Média'] >= 6:
            resp['Situação'] = 'Razoável'
        else:
            resp['Situação'] = 'Ruim'
    
    return resp  # Retorna o dicionário com as informações

# Lista para armazenar as notas
notas_list = list()

# Loop para capturar as notas dos alunos
while True:
    valor = input("Insira a nota: ")
    while not valor.replace('.', '', 1).isdigit():  # Verifica se o valor é numérico
        print("ERRO! Insira um valor numérico!")
        valor = input("Insira a nota: ")
    notas_list.append(float(valor))  # Adiciona a nota à lista
    continuar = input("Deseja Continuar? [S/N]: ").strip().lower()
    if continuar == 'n':  # Se 'n', termina o loop
        break

# Pergunta ao usuário se deseja mostrar a situação da classe
sit = str(input("Deseja mostrar a situação da classe? [S/N]: ")).strip().lower()
while sit not in 'sn':  # Valida a resposta
    print("ERRO! Responda com S ou N")
    sit = str(input("Deseja mostrar a situação da classe? [S/N]: ")).strip().lower()

# Exibe os resultados, desempacotando a lista de notas
if sit == 's':
    print(notas(*notas_list, b=True))  # Chama a função com situação
else:
    print(notas(*notas_list))  # Chama a função sem a situação

