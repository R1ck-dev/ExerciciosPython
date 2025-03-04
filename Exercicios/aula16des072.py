# Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

# Dicionário de cores para formatação do texto no terminal
cores = {'limpa': '\033[m', 'titulo': '\033[1;35m',
         'vermelho': '\033[31m', 'verde': '\033[32m', 'azul': '\033[34m'}

# Exibição do título do exercício
print('-=*=-' * 10)
print(' ' * 18, f"{cores['titulo']}EXERCICIO 72{cores['limpa']}")
print('-=*=-' * 10)

# Tupla com os valores por extenso de 0 a 20
valores = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez",
           "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")

# Loop para validar a entrada do usuário
while True:
    entrada = int(input("Insira o valor [0 a 20] que deseja ver por extenso: "))
    if entrada < 0 or entrada > 20:
        print(f"{cores['vermelho']}Valor fora de alcance, tente novamente!{cores['limpa']}")
    else:
        break  # Sai do loop se a entrada estiver dentro do intervalo

# Exibe o número digitado por extenso
print(f"\n{cores['azul']}{valores[entrada]}{cores['limpa']}")
