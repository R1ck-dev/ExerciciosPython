from datetime import datetime

cores = {'limpa': '\033[m', 'titulo': '\033[1;35m',
         'vermelho': '\033[31m', 'verde': '\033[32m', 'azul': '\033[34m'}

print('-=*=-' * 10)
print(f"{cores['titulo']}EXERCICIO 92{cores['limpa']}".center(60))
print('-=*=-' * 10)

dados = dict()

dados['nome'] = str(input('Nome: '))
dados['nascimento'] = int(input('Ano de Nascimento: '))
dados['idade'] = datetime.now().year - dados['nascimento']
dados['ctps'] = int(input('Carteira de Trabalho (0 = não tem): '))
if dados['ctps'] == 0:
    for k, v in dados.items():
        print(f'- {k} tem o valor {v}')
dados['contratação'] = int(input('Ano de Contratação: '))
dados['salário'] = float(input('Salário: '))
dados['aposetandoria'] = dados['idade'] + ((dados['contratação'] + 35) - datetime.now().year)
for k, v in dados.items():
    print(f'- {k} tem o valor {v}')
