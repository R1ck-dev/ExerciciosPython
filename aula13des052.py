cores = {'limpa':'\033[m', 'titulo':'\033[1;35m',
         'vermelho':'\033[31m', 'verde':'\033[32m', 'azul':'\033[34m'}

print('-=*=-'*10)
print(' '*18 , '{}EXERCICIO 52{}'.format(cores['titulo'], cores['limpa']))
print('-=*=-'*10)

valor = int(input('Insira um valor qualquer: '))
p_np = 0

for c in range(2, valor):
    if valor % c == 0:
        p_np = 1

if p_np != 0:
    print('{}{}{} {}não é primo{}'.format(cores['titulo'], valor, cores['limpa'],
                                            cores['vermelho'], cores['limpa']))
else:
    print('{}{}{} {}é primo{}'.format(cores['titulo'], valor, cores['limpa'],
                                            cores['azul'], cores['limpa']))

