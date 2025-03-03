from des_moedas import aula22des108

def metade(num, b=False):
    num = num/2
    if b:
        num = aula22des108.formatar(num)
    return num


def dobro(num, b=False):
    num = num * 2
    if b:
        num = aula22des108.formatar(num)
    return num


def aumentando(num, aum, b=False):
    num = num+(num*(aum/100))
    if b:
        num = aula22des108.formatar(num)
    return num


def diminuindo(num, des, b=False):
    num = num-(num*(des/100))
    if b:
        num = aula22des108.formatar(num)
    return num