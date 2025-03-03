cores = {'limpa': '\033[m', 'titulo': '\033[1;35m',
         'vermelho': '\033[31m', 'verde': '\033[32m', 'azul': '\033[34m'}

print('-=*=-' * 10)
print(' ' * 18, f"{cores['titulo']}EXERCICIO 73{cores['limpa']}")
print('-=*=-' * 10)

campeonato_brasileiro = ("botafogo", "palmeiras", "flamengo", "fortaleza", "internacional", "são paulo", "corinthians",
                         "bahia", "cruzeiro", "vasco", "vitória", "chapecoense", "atlético mineiro", "fluminense", "gremio", "juventude",
                         "bragantino", "atlético paranaense", "criciúma", "atlético goianiense", "cuiabá")

print(f"{cores['titulo']}Campeonato Brasileiro:{cores['limpa']} \n{cores['azul']}{campeonato_brasileiro}{cores['limpa']}")
print('-=*=-' * 10)
print(f"{cores['titulo']}Os cinco primeiros colocados são:{cores['limpa']} {cores['azul']}{campeonato_brasileiro[:5]}{cores['limpa']}")
print('-=*=-' * 10)
print(f"{cores['titulo']}Os cinco últimos colocados são:{cores['limpa']} {cores['azul']}{campeonato_brasileiro[-5:]}{cores['limpa']}")
print('-=*=-' * 10)
print(f"{cores['titulo']}A lista do campeonato brasileiro em ordem alfabética:{cores['limpa']} \n{cores['azul']}{sorted(campeonato_brasileiro)}{cores['limpa']}")
print('-=*=-' * 10)
for pos, time in enumerate(campeonato_brasileiro):
    if time == "chapecoense":
        print(f"{cores['titulo']}A posição da {time} é [{pos+1}° colocado]{cores['limpa']}")
