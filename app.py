import os

class Restaurante:
    def __init__(self, nome, categoria):
        # Inicializa um novo Restaurante com nome, categoria e ativo
        self.nome = nome
        self.categoria = categoria
        self.ativo = False

    def __str__(self):
        # Retorna uma representação em string do objeto Restaurante
        status = 'ativado' if self.ativo else 'desativado'
        return f'- {self.nome.ljust(20)} | {self.categoria.ljust(20)} | {status}'

# Lista de restaurantes pré-definidos
restaurantes = [
    Restaurante('Praça', 'Japonesa'),
    Restaurante('Pizza Suprema', 'Pizza'),
    Restaurante('Cantina', 'Italiano')
]

def exibir_nome_do_programa():
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
""")

def exibir_opcoes():
    # Exibe as opções do menu principal
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Alternar estado do restaurante')
    print('4. Sair\n')

def finalizar_app():
    # Exibe subtítulo de finalização do aplicativo para voltar ao menu principal
    exibir_subtitulo('Finalizar app')
    print("Aplicativo finalizado.")
    exit()

def voltar_ao_menu_principal():
    # Espera a entrada do usuário para voltar ao menu principal
    input('\nDigite uma tecla para voltar ao menu ')
    main()

def opcao_invalida():
    # Exibe mensagem de opção inválida e volta ao menu principal
    print('Opção inválida!\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    # Limpa a tela e exibe um subtítulo com base no texto fornecido
    os.system('cls' if os.name == 'nt' else 'clear')
    linha = '*' * len(texto)
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_novo_restaurante():
    # Permite o cadastro de um novo restaurante
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite a categoria do restaurante {nome_do_restaurante}: ')
    novo_restaurante = Restaurante(nome_do_restaurante, categoria)
    restaurantes.append(novo_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    
    voltar_ao_menu_principal()

def listar_restaurantes():
    # Lista todos os restaurantes com suas categorias e status
    exibir_subtitulo('Listando restaurantes')
    print(f'{"Nome do restaurante".ljust(22)} | {"Categoria".ljust(20)} | Status')
    for restaurante in restaurantes:
        print(restaurante)
    voltar_ao_menu_principal()

def alternar_estado_restaurante():
    # Permite alterar o estados (ativo/desativado) de um restaurante
    exibir_subtitulo('Alterando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante.nome:
            restaurante_encontrado = True
            restaurante.ativo = not restaurante.ativo
            status = 'ativado' if restaurante.ativo else 'desativado'
            print(f'O restaurante {nome_restaurante} foi {status} com sucesso!')
            break
            
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado.')
            
    voltar_ao_menu_principal()

def escolher_opcao():
    # Permite ao usuário escolher uma opção e chama a função correspondente
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        if opcao_escolhida == 1: 
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2: 
            listar_restaurantes()
        elif opcao_escolhida == 3: 
            alternar_estado_restaurante()
        elif opcao_escolhida == 4: 
            finalizar_app()
        else: 
            opcao_invalida()
    except ValueError:
        opcao_invalida()

def main():
    # Função principal que chama o menu principal e permite escolher opções
    os.system('cls' if os.name == 'nt' else 'clear')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    # Ponto de entrada do programa
    main()
