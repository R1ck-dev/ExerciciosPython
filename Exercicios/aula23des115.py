# Arquivos com Python

# Definição das cores para personalizar a saída do terminal
cores = {
    'limpa': '\033[m',         # Reseta todas as cores/formatações
    'titulo': '\033[1;35m',     # Roxo em negrito
    'vermelho': '\033[31m',     # Vermelho normal
    'verde': '\033[32m',        # Verde normal
    'azul': '\033[34m',         # Azul normal
    'amarelo': '\033[33m',      # Amarelo normal
    'ciano': '\033[36m',        # Ciano normal
    'magenta': '\033[35m',      # Magenta normal
    'branco': '\033[97m',       # Branco normal
    'preto': '\033[30m',        # Preto normal

    # Negrito
    'vermelho_b': '\033[1;31m',
    'verde_b': '\033[1;32m',
    'azul_b': '\033[1;34m',
    'amarelo_b': '\033[1;33m',
    'ciano_b': '\033[1;36m',
    'magenta_b': '\033[1;35m',
    'branco_b': '\033[1;97m',
    'preto_b': '\033[1;30m',
}

# Exibe uma linha de separação com as cores do terminal
print('-=*=-' * 10)
# Exibe o título "EXERCÍCIO 115" centralizado com cor roxa
print(f"{cores['titulo']}EXERCICIO 115{cores['limpa']}".center(60))
# Exibe outra linha de separação
print('-=*=-' * 10)

# Função para exibir uma linha de separação
def linha():
    # A linha será composta por '-' coloridos em branco
    print(f'{cores["branco_b"]}-{cores["limpa"]}' * 30)

# Função para exibir o título do menu principal
def menu_art():
    linha()  # Chama a função linha() para exibir uma linha de separação
    print(f'{cores["ciano_b"]}{"MENU PRINCIPAL":^30}{cores["limpa"]}')  # Exibe o título centralizado com cor ciano
    linha()  # Chama a função linha() novamente para exibir outra linha de separação

# Função principal que exibe o menu e lida com as opções do usuário
def menu_esc():
    try:
        # Tenta criar um arquivo chamado 'cadastro.txt' no modo de escrita (com 'x' para garantir que o arquivo não exista)
        with open('cadastro.txt', 'x', encoding='utf-8') as f:
            print(f'\n{cores["verde_b"]}Arquivo Criado{cores["limpa"]}')  # Exibe mensagem confirmando que o arquivo foi criado
    except FileExistsError:
        # Se o arquivo já existir, exibe o menu de opções
        menu_art()  # Exibe o título do menu
        print(f'{cores["branco_b"]}1 -{cores["limpa"]} {cores["azul"]}Ver Pessoas Cadastradas{cores["limpa"]}')
        print(f'{cores["branco_b"]}2 -{cores["limpa"]} {cores["azul"]}Cadastrar Nova Pessoa{cores["limpa"]}')
        print(f'{cores["branco_b"]}3 -{cores["limpa"]} {cores["azul"]}Sair do Sistema{cores["limpa"]}')
        
        # Variável global opc para armazenar a escolha do usuário
        global opc
        linha()  # Exibe uma linha de separação

        while True:
            try:
                # Solicita a entrada de uma opção do usuário
                opc = int(input(f'{cores["amarelo_b"]}Sua Opção:{cores["limpa"]} '))
                # Verifica se a opção é válida (1, 2 ou 3)
                if str(opc) not in '123':
                    raise ValueError  # Lança erro se a opção não for válida
                break
            except ValueError:
                # Caso o usuário digite uma opção inválida
                print(f'{cores["vermelho_b"]}ERRO! Digite uma Opção Válida{cores["limpa"]}')

        # Ações para cada opção escolhida
        if opc == 1:
            linha()  # Exibe linha de separação
            print(f'{cores["ciano_b"]}{"PESSOAS CADASTRADAS":^30}{cores["limpa"]}')  # Título para pessoas cadastradas
            linha()  # Exibe outra linha de separação
            with open('cadastro.txt', 'r', encoding='utf-8') as f:
                # Abre o arquivo em modo leitura e exibe cada linha
                for linha_ in f:
                    print(linha_, end='')

        if opc == 2:
            linha()  # Exibe linha de separação
            print(f'{cores["ciano_b"]}{"NOVO CADASTRO":^30}{cores["limpa"]}')  # Título para novo cadastro
            linha()  # Exibe outra linha de separação
            with open('cadastro.txt', 'a', encoding='utf-8') as f:
                # Abre o arquivo em modo de adição
                nome = str(input(f"{cores['amarelo_b']}Nome:{cores['limpa']} "))  # Solicita o nome do novo cadastro
                while True:
                    try:
                        idade = int(input(f"{cores['amarelo_b']}Idade: {cores['limpa']}"))  # Solicita a idade e garante que seja um inteiro
                        break
                    except ValueError:
                        # Caso o valor da idade não seja válido
                        print(f'{cores["vermelho_b"]}ERRO! Digite um número inteiro válido.{cores["limpa"]}')
                # Escreve no arquivo o nome e idade formatados
                f.write(f'{nome.ljust(24)}{str(idade).rjust(2)} anos\n')
                # Confirma o registro
                print(f'{cores["azul"]}Novo registro de {nome} adicionado{cores["limpa"]}')

        if opc == 3:
            linha()  # Exibe linha de separação
            print(f'{cores["ciano_b"]}{"Saindo do Sistema... Até Logo!":^30}{cores["limpa"]}')  # Mensagem de saída
            linha()  # Exibe última linha de separação

# Variável opc para controlar o menu
opc = 0

# Loop principal para exibir o menu repetidamente até o usuário escolher a opção de sair
while True:
    menu_esc()  # Exibe o menu
    print()
    if opc == 3:  # Se a opção for 3 (sair), quebra o loop
        break
