# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.

# Importa o módulo datetime para obter o ano atual
from datetime import datetime

# Dicionário com códigos ANSI para colorir a saída no terminal
cores = {'limpa': '\033[m', 'titulo': '\033[1;35m',
         'vermelho': '\033[31m', 'verde': '\033[32m', 'azul': '\033[34m'}

# Impressão do título formatado do exercício
print('-=*=-' * 10)
print(f"{cores['titulo']}EXERCICIO 101{cores['limpa']}".center(60))
print('-=*=-' * 10)

# Função que recebe o ano de nascimento e retorna o tipo de voto (Obrigatório, Opcional ou Negado)
def voto(a):
    # A variável 'idade' foi calculada fora da função, mas dentro da função 'voto', 'idade' não está definida.
    # Deveria verificar a 'idade' dentro da função, não o parâmetro 'a'
    if idade > 18 and idade < 65:  # Idade entre 18 e 65 anos tem voto obrigatório
        return 'Voto Obrigatório'
    elif idade < 0:  # Caso a idade seja negativa, retorna erro
        return 'Erro!'
    else:  # Para idades abaixo de 18 ou acima de 65, o voto é opcional
        return 'Voto Opcional'


# Solicita o ano de nascimento do usuário
ano_nasc = int(input("Ano de Nascimento: "))

# Calcula a idade da pessoa com base no ano atual
idade = datetime.now().year - ano_nasc

# Exibe a idade e o tipo de voto com base na idade
print(f'Com {idade} anos: {voto(ano_nasc)}')

