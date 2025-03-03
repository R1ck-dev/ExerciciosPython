cores = {'limpa': '\033[m', 'titulo': '\033[1;35m',
         'vermelho': '\033[31m', 'verde': '\033[32m', 'azul': '\033[34m'}

print('-=*=-' * 10)
print(f"{cores['titulo']}EXERCICIO 94{cores['limpa']}".center(60))
print('-=*=-' * 10)

cadastro = dict()
cadastro_list = list()
soma_idade = 0
listF = list()

while True:
    cadastro['nome'] = str(input('Nome: '))
    cadastro['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()
    while cadastro['sexo'] not in 'FM':
        print("ERRO! Por favor, digite apenas M ou F.")
        cadastro['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()
    if cadastro['sexo'] == 'F':
        listF.append(cadastro['nome'])
    cadastro['idade'] = int(input('Idade: '))
    soma_idade += cadastro['idade']
    continuar = str(input("Continuar? [S/N]: ")).strip().upper()
    while continuar not in 'SN':
        print("ERRO! Responda apenas S ou N.")
        continuar = str(input("Continuar? [S/N]: ")).strip().upper()
    cadastro_list.append(cadastro.copy())
    if continuar == 'N':
        break
print('-=' * 45)
print(f'A) Ao todo temos {len(cadastro_list)} pessoas cadastradas.')
print(f'B) A média de idade é de {soma_idade/len(cadastro_list):.2f}')
print(f'C) As mulheres cadastradas foram {listF}')
list_temp = list()
list_maiores_media = list()
for c in range(0, len(cadastro_list)):
    if cadastro_list[c]['idade'] > soma_idade/len(cadastro_list):
        list_temp.append(cadastro_list[c]['nome'][:])
        list_temp.append(cadastro_list[c]['sexo'][:])
        list_temp.append(cadastro_list[c]['idade'])
        list_maiores_media.append(list_temp[:])
        list_temp.clear()
print('D) Lista das pessoas que estão acima da média de idade:')
for c in range(0, len(list_maiores_media)):
    print(f'{"":>3} nome = {list_maiores_media[c][0]}; sexo = {list_maiores_media[c][1]}; idade = {list_maiores_media[c][2]}')
print('<< ENCERRADO >>')