cores = {'limpa': '\033[m', 'titulo': '\033[1;35m',
         'vermelho': '\033[31m', 'verde': '\033[32m', 'azul': '\033[34m'}

print('-=*=-' * 10)
print(f"{cores['titulo']}EXERCICIO 113{cores['limpa']}".center(60))
print('-=*=-' * 10)

def leiaint(msg):
    while True:
        try:
            valor = int(input(msg))
            return valor
        except ValueError:
            print(f"{cores['vermelho']}ERRO! {cores['limpa']}", end='')


def leiafloat(msg):
    while True:
        try:
            valor = (input(msg))
            if '.' not in valor:
                raise ValueError
            return float(valor)
        except ValueError:
            print(f"{cores['vermelho']}ERRO! {cores['limpa']}", end='')
        except KeyboardInterrupt:
            print(f"{cores['vermelho']}O Usuário Encerrou o Programa {cores['limpa']}")
            return 0

n = leiaint("Digite um número inteiro: ")
f = leiafloat("Digite um número real: ")
print(f"Você acabou de digitar o número {n} inteiro e o numero {f} real")

