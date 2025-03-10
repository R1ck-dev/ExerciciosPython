# Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante ‘a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)

# Dicionário com códigos ANSI para colorir a saída no terminal
cores = {'limpa': '\033[m', 'titulo': '\033[1;35m',
         'vermelho': '\033[31m', 'verde': '\033[32m', 'azul': '\033[34m'}

# Impressão do título formatado do exercício
print('-=*=-' * 10)
print(f"{cores['titulo']}EXERCICIO 104{cores['limpa']}".center(60))
print('-=*=-' * 10)

# Função leiaint que recebe uma entrada e valida se é um número
def leiaint(a):
    """
    Função para garantir que a entrada seja um número válido
    :param a: Entrada fornecida pelo usuário (string)
    :return: A entrada convertida para número (se válida)
    """
    while not a.isnumeric():  # Enquanto a entrada não for numérica
        # Exibe uma mensagem de erro em vermelho caso o valor não seja numérico
        print(f"{cores['vermelho']}ERRO! Digite um número: {cores['limpa']}", end='') 
        a = input()  # Solicita nova entrada ao usuário
    return a  # Retorna o valor quando for um número válido

# Chama a função leiaint com a entrada do usuário
valor = leiaint(input("Digite um número: "))  
print(f"Você acabou de digitar o número {valor}")  # Exibe o número digitado
