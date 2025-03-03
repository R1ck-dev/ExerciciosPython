from UltimoDesafio.cores import cores_

cores = cores_()

def linha():
    print(f'{cores["branco_b"]}-{cores["limpa"]}' * 30)

def menu_art():
    linha()
    print(f'{cores["ciano_b"]}{"MENU PRINCIPAL":^30}{cores["limpa"]}')
    linha()

def menu_esc():
    try:
        with open('cadastro.txt', 'x', encoding='utf-8') as f:
            print(f'\n{cores["verde_b"]}Arquivo Criado{cores["limpa"]}')
    except FileExistsError:
        menu_art()
        print(f'{cores["branco_b"]}1 -{cores["limpa"]} {cores["azul"]}Ver Pessoas Cadastradas{cores["limpa"]}')
        print(f'{cores["branco_b"]}2 -{cores["limpa"]} {cores["azul"]}Cadastrar Nova Pessoa{cores["limpa"]}')
        print(f'{cores["branco_b"]}3 -{cores["limpa"]} {cores["azul"]}Sair do Sistema{cores["limpa"]}')
        global opc
        linha()
        while True:
            try:
                opc = int(input(f'{cores["amarelo_b"]}Sua Opção:{cores["limpa"]} '))
                if str(opc) not in '123':
                    raise ValueError
                break
            except ValueError:
                print(f'{cores["vermelho_b"]}ERRO! Digite uma Opção Válida{cores["limpa"]}')
        if opc == 1:
            linha()
            print(f'{cores["ciano_b"]}{"PESSOAS CADASTRADAS":^30}{cores["limpa"]}')
            linha()
            with open('cadastro.txt', 'r', encoding='utf-8') as f:
                for linha_ in f:
                    print(linha_, end='')
        if opc == 2:
            linha()
            print(f'{cores["ciano_b"]}{"NOVO CADASTRO":^30}{cores["limpa"]}')
            linha()
            with open('cadastro.txt', 'a', encoding='utf-8') as f:
                nome = str(input(f"{cores['amarelo_b']}Nome:{cores['limpa']} "))
                while True:
                    try:
                        idade = int(input(f"{cores['amarelo_b']}Idade: {cores['limpa']}"))
                        break
                    except ValueError:
                        print(f'{cores["vermelho_b"]}ERRO! Digite um número inteiro válido.{cores["limpa"]}')
                f.write(f'{nome.ljust(24)}{str(idade).rjust(2)} anos\n')
                print(f'{cores["azul"]}Novo registro de {nome} adicionado{cores["limpa"]}')
        if opc == 3:
            linha()
            print(f'{cores["ciano_b"]}{"Saindo do Sistema... Até Logo!":^30}{cores["limpa"]}')
            linha()