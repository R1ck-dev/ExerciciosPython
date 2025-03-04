# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: A) Quantas pessoas foram cadastradas B) A média de idade C) Uma lista com as mulheres D) Uma lista de pessoas com idade acima da média

# Dicionário contendo códigos ANSI para colorir a saída no terminal
cores = {'limpa': '\033[m', 'titulo': '\033[1;35m',
         'vermelho': '\033[31m', 'verde': '\033[32m', 'azul': '\033[34m'}

# Impressão do título formatado do exercício
print('-=*=-' * 10)
print(f"{cores['titulo']}EXERCICIO 94{cores['limpa']}".center(60))
print('-=*=-' * 10)

# Declaração das estruturas de dados
cadastro = dict()  # Dicionário para armazenar os dados de uma pessoa
cadastro_list = list()  # Lista para armazenar os dicionários de todas as pessoas cadastradas
soma_idade = 0  # Variável para calcular a soma das idades
listF = list()  # Lista para armazenar os nomes das mulheres cadastradas

# Loop para cadastro das pessoas
while True:
    cadastro['nome'] = str(input('Nome: '))  # Entrada do nome

    # Entrada do sexo, garantindo que seja 'M' ou 'F'
    cadastro['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()
    while cadastro['sexo'] not in 'FM':
        print("ERRO! Por favor, digite apenas M ou F.")
        cadastro['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()

    # Se for mulher, adiciona o nome à lista de mulheres
    if cadastro['sexo'] == 'F':
        listF.append(cadastro['nome'])

    # Entrada da idade e soma para o cálculo da média
    cadastro['idade'] = int(input('Idade: '))
    soma_idade += cadastro['idade']

    # Pergunta se deseja continuar cadastrando
    continuar = str(input("Continuar? [S/N]: ")).strip().upper()
    while continuar not in 'SN':
        print("ERRO! Responda apenas S ou N.")
        continuar = str(input("Continuar? [S/N]: ")).strip().upper()

    # Adiciona a cópia do dicionário à lista principal
    cadastro_list.append(cadastro.copy())

    # Encerra o loop se o usuário não quiser continuar
    if continuar == 'N':
        break

# Exibição dos resultados
print('-=' * 45)
print(f'A) Ao todo temos {len(cadastro_list)} pessoas cadastradas.')
print(f'B) A média de idade é de {soma_idade / len(cadastro_list):.2f}')
print(f'C) As mulheres cadastradas foram {listF}')

# Criação de uma lista para armazenar pessoas com idade acima da média
list_temp = list()
list_maiores_media = list()
for c in range(0, len(cadastro_list)):
    if cadastro_list[c]['idade'] > soma_idade / len(cadastro_list):
        list_temp.append(cadastro_list[c]['nome'][:])  # Adiciona nome
        list_temp.append(cadastro_list[c]['sexo'][:])  # Adiciona sexo
        list_temp.append(cadastro_list[c]['idade'])  # Adiciona idade
        list_maiores_media.append(list_temp[:])  # Adiciona à lista principal
        list_temp.clear()  # Limpa a lista temporária

# Exibe a lista de pessoas com idade acima da média
print('D) Lista das pessoas que estão acima da média de idade:')
for c in range(0, len(list_maiores_media)):
    print(
        f'{"":>3} nome = {list_maiores_media[c][0]}; sexo = {list_maiores_media[c][1]}; idade = {list_maiores_media[c][2]}')

# Finaliza o programa
print('<< ENCERRADO >>')
