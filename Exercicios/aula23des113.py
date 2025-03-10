# Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.

# Dicionário com códigos ANSI para colorir a saída no terminal
cores = {'limpa': '\033[m', 'titulo': '\033[1;35m',
         'vermelho': '\033[31m', 'verde': '\033[32m', 'azul': '\033[34m'}

# Impressão do título formatado do exercício
print('-=*=-' * 10)
print(f"{cores['titulo']}EXERCICIO 113{cores['limpa']}".center(60))
print('-=*=-' * 10)

# Função para ler um número inteiro com validação
def leiaint(msg):
    while True:
        try:
            valor = int(input(msg))  # Tenta converter a entrada para inteiro
            return valor  # Retorna o valor caso seja um número inteiro válido
        except ValueError:
            print(f"{cores['vermelho']}ERRO! Digite um número inteiro válido.{cores['limpa']}")  # Mensagem de erro

# Função para ler um número real (float) com validação
def leiafloat(msg):
    while True:
        try:
            valor = input(msg)  # Lê a entrada do usuário
            valor = valor.replace(',', '.')  # Substitui vírgula por ponto (caso o usuário digite)
            return float(valor)  # Tenta converter para float e retorna
        except ValueError:
            print(f"{cores['vermelho']}ERRO! Digite um número real válido.{cores['limpa']}")  # Mensagem de erro
        except KeyboardInterrupt:
            print(f"{cores['vermelho']}O usuário encerrou o programa.{cores['limpa']}")
            return 0  # Retorna 0 caso o usuário interrompa o programa com Ctrl+C

# Leitura de valores com validação
n = leiaint("Digite um número inteiro: ")
f = leiafloat("Digite um número real: ")

# Exibição do resultado
print(f"Você acabou de digitar o número {n} inteiro e o número {f} real.")


