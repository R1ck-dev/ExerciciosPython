# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import datetime  # Importa a classe datetime para obter o ano atual

# Dicionário contendo códigos ANSI para colorir a saída no terminal
cores = {'limpa': '\033[m', 'titulo': '\033[1;35m',
         'vermelho': '\033[31m', 'verde': '\033[32m', 'azul': '\033[34m'}

# Impressão do título formatado do exercício
print('-=*=-' * 10)
print(f"{cores['titulo']}EXERCICIO 92{cores['limpa']}".center(60))
print('-=*=-' * 10)

# Dicionário para armazenar os dados do trabalhador
dados = dict()

# Coleta do nome e ano de nascimento
dados['nome'] = str(input('Nome: '))
dados['nascimento'] = int(input('Ano de Nascimento: '))

# Cálculo da idade com base no ano atual
dados['idade'] = datetime.now().year - dados['nascimento']

# Coleta do número da Carteira de Trabalho (CTPS)
dados['ctps'] = int(input('Carteira de Trabalho (0 = não tem): '))

# Se a CTPS for 0, exibe apenas os dados coletados até aqui e encerra a exibição
if dados['ctps'] == 0:
    for k, v in dados.items():
        print(f'- {k} tem o valor {v}')
else:
    # Coleta do ano de contratação e salário caso o trabalhador tenha CTPS
    dados['contratação'] = int(input('Ano de Contratação: '))
    dados['salário'] = float(input('Salário: '))

    # Cálculo da idade da aposentadoria (35 anos de contribuição após a contratação)
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - datetime.now().year)

    # Exibição de todos os dados coletados
    for k, v in dados.items():
        print(f'- {k} tem o valor {v}')

