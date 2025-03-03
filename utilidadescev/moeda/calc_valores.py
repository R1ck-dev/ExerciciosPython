from utilidadescev.moeda.formatar import formatar

def metade(num, b=False):
    num = num/2
    if b:
        num = formatar(num)
    return num


def dobro(num, b=False):
    num = num * 2
    if b:
        num = formatar(num)
    return num


def aumentando(num, aum, b=False):
    num = num+(num*(aum/100))
    if b:
        num = formatar(num)
    return num


def diminuindo(num, des, b=False):
    num = num-(num*(des/100))
    if b:
        num = formatar(num)
    return num