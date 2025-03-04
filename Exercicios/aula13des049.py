# Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

# Dicionário contendo códigos ANSI para formatação de cores no terminal
cores = {'limpa':'\033[m', 'titulo':'\033[1;35m',
         'vermelho':'\033[31m', 'verde':'\033[32m', 'azul':'\033[34m'}

# Exibição do cabeçalho do exercício formatado com cores
print('-=*=-'*10)
print(' '*18 , '{}EXERCICIO 49{}'.format(cores['titulo'], cores['limpa']))
print('-=*=-'*10)

# Solicita ao usuário qual tabuada ele deseja visualizar
tab = int(input('Indique qual tabuada deseja acessar: '))

# Laço que percorre os números de 0 a 10 para exibir a tabuada escolhida
for c in range (0, 11):
    # Exibe a multiplicação formatada com cores
    print('{}{}{} x {} = {}{}{}'.format(cores['vermelho'], tab, cores['limpa'],
                                            c, cores['titulo'], tab*c, cores['limpa']))
