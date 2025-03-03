cores = {'limpa': '\033[m', 'titulo': '\033[1;35m',
         'vermelho': '\033[31m', 'verde': '\033[32m', 'azul': '\033[34m'}

print('-=*=-' * 10)
print(' ' * 18, f"{cores['titulo']}EXERCICIO 69{cores['limpa']}")
print('-=*=-' * 10)

cont_mais18 = qtd_homens = qtd_mulheres20 = 0

while True:
    # Validação da idade
    while True:
        try:
            idade = int(input('Insira a idade: '))
            break
        except ValueError:
            print('Entrada inválida! Insira a idade: ')

    # Verifica maiores de 18 anos
    if idade > 18:
        cont_mais18 += 1

    # Validação do sexo
    sexo = input('Insira o sexo [f/m]: ').lower()
    while sexo not in ['m', 'f']:
        sexo = input('Entrada inválida! Insira o sexo [f/m]: ').lower()

    if sexo == 'm':
        qtd_homens += 1
    elif sexo == 'f' and idade < 20:
        qtd_mulheres20 += 1

    # Validação para continuar
    continuar = input('Deseja continuar [s/n]: ').lower()
    while continuar not in ['s', 'n']:
        continuar = input('Entrada inválida! Deseja continuar [s/n]: ').lower()

    print(f"{cores['titulo']}-=*=-{cores['limpa']}" * 10)
    if continuar == 'n':
        break

# Exibição dos resultados
print('Programa Finalizado!')
print(f'Quantidade de Homens = {qtd_homens}')
print(f'Homens maiores de 18 anos = {cont_mais18}')
print(f'Mulheres com menos de 20 anos = {qtd_mulheres20}')
