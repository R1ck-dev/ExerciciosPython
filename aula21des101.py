from datetime import datetime

cores = {'limpa': '\033[m', 'titulo': '\033[1;35m',
         'vermelho': '\033[31m', 'verde': '\033[32m', 'azul': '\033[34m'}

print('-=*=-' * 10)
print(f"{cores['titulo']}EXERCICIO 101{cores['limpa']}".center(60))
print('-=*=-' * 10)

def voto(a):
    if idade > 18 and idade < 65:
        return 'Voto Obrigatório'
    elif idade < 0:
        return 'Erro!'
    else:
        return 'Voto Opcional'


ano_nasc = int(input("Ano de Nascimento: "))
idade = datetime.now().year - ano_nasc
print(f'Com {idade} anos: {voto(ano_nasc)}')
