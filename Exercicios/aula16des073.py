# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
#
# a) Os 5 primeiros times.
#
# b) Os últimos 4 colocados.
#
# c) Times em ordem alfabética.
#
# d) Em que posição está o time da Chapecoense.

# Dicionário de cores para formatação do texto no terminal
cores = {'limpa': '\033[m', 'titulo': '\033[1;35m',
         'vermelho': '\033[31m', 'verde': '\033[32m', 'azul': '\033[34m'}

# Exibição do título do exercício
print('-=*=-' * 10)
print(' ' * 18, f"{cores['titulo']}EXERCICIO 73{cores['limpa']}")
print('-=*=-' * 10)

# Tupla contendo os 20 primeiros times do Campeonato Brasileiro
campeonato_brasileiro = ("botafogo", "palmeiras", "flamengo", "fortaleza", "internacional", "são paulo", "corinthians",
                         "bahia", "cruzeiro", "vasco", "vitória", "chapecoense", "atlético mineiro", "fluminense", "gremio",
                         "juventude", "bragantino", "atlético paranaense", "criciúma", "atlético goianiense", "cuiabá")

# Exibe a lista completa dos times
print(f"{cores['titulo']}Campeonato Brasileiro:{cores['limpa']} \n{cores['azul']}{campeonato_brasileiro}{cores['limpa']}")
print('-=*=-' * 10)

# Exibe os cinco primeiros colocados
print(f"{cores['titulo']}Os cinco primeiros colocados são:{cores['limpa']} {cores['azul']}{campeonato_brasileiro[:5]}{cores['limpa']}")
print('-=*=-' * 10)

# Exibe os cinco últimos colocados
print(f"{cores['titulo']}Os cinco últimos colocados são:{cores['limpa']} {cores['azul']}{campeonato_brasileiro[-5:]}{cores['limpa']}")
print('-=*=-' * 10)

# Exibe os times em ordem alfabética
print(f"{cores['titulo']}A lista do campeonato brasileiro em ordem alfabética:{cores['limpa']} \n{cores['azul']}{sorted(campeonato_brasileiro)}{cores['limpa']}")
print('-=*=-' * 10)

# Busca a posição do time Chapecoense na lista
for pos, time in enumerate(campeonato_brasileiro):
    if time == "chapecoense":
        print(f"{cores['titulo']}A posição da {time} é [{pos+1}° colocado]{cores['limpa']}")

