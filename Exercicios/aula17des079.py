# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

# Dicionário contendo códigos ANSI para colorir a saída no terminal
cores = {'limpa': '\033[m', 'titulo': '\033[1;35m',
         'vermelho': '\033[31m', 'verde': '\033[32m', 'azul': '\033[34m'}

# Impressão do título formatado do exercício
print('-=*=-' * 10)
print(f"{cores['titulo']}EXERCICIO 79{cores['limpa']}".center(60))
print('-=*=-' * 10)

# Criando uma lista vazia para armazenar os valores únicos
valores = []

# Variável de controle para continuar ou parar o loop
continuar = ''

# Loop infinito para entrada de valores
while True:
    num = int(input("Digite um valor: "))  # Lendo um número inteiro do usuário

    if num in valores:  # Verificando se o número já está na lista
        print("Valor já existente!")  # Caso exista, não adiciona e avisa o usuário
    else:
        valores.append(num)  # Se for novo, adiciona à lista

    # Pergunta ao usuário se deseja continuar
    continuar = input("Deseja continuar? (S/N): ").upper()

    # Se a resposta não for 'S', o loop será interrompido
    if continuar != 'S':
        break

# Ordenando a lista antes de exibi-la
valores.sort()

# Exibindo os valores únicos em ordem crescente
print(valores)
