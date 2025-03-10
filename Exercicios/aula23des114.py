# Crie um código em Python que teste se o site pudim está acessível pelo computador usado.

import requests

cores = {'limpa': '\033[m', 'titulo': '\033[1;35m',
         'vermelho': '\033[31m', 'verde': '\033[32m', 'azul': '\033[34m'}

print('-=*=-' * 10)
print(f"{cores['titulo']}EXERCICIO 114{cores['limpa']}".center(60))
print('-=*=-' * 10)

def verificar(msg):
    print(msg)
    site = str(input())
    try:
        resposta = requests.get(site, timeout=5)
        if resposta.status_code == 200:
            print(f'O site {site} está acessível.')
        else:
            print(f'O site {site} retornou status code {resposta.status_code}.')
    except requests.ConnectTimeout:
        print('Tempor de Conexão Excedido')
    except requests.ConnectionError:
        print('Erro de Conexão')
    except requests.RequestException as error:
        print(f'Ocorreu um erro ao acessar {site} : {error}')


verificar("Qual site deseja verificar? ")
