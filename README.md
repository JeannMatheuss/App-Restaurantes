***Sistema de Gerenciamento de Restaurantes***

Este projeto é um sistema de gerenciamento de restaurantes que permite aos usuários cadastrar, listar e alterar o estado (ativo/desativado) de restaurantes. O sistema é baseado em um menu interativo com opções para executar as funcionalidades mencionadas.

***Funcionalidades***

O sistema oferece as seguintes funcionalidades:

Cadastrar Restaurante: Permite ao usuário cadastrar um novo restaurante com um nome e categoria especificados.

Listar Restaurantes: Exibe uma lista de todos os restaurantes cadastrados, com suas categorias e status (ativo ou desativado).

Alternar Estado do Restaurante: Permite ao usuário alternar o estado (ativo/desativado) de um restaurante específico, identificado pelo nome.

Sair: Permite ao usuário sair do programa.

***Estrutura do Código***

O sistema é composto pelas seguintes partes:

Classe Restaurante: Representa cada restaurante com atributos nome, categoria e ativo. Inclui um método __str__ que retorna uma representação em string do restaurante.

Menu Principal: A função main() exibe o menu principal com as opções disponíveis e permite ao usuário escolher uma opção para executar.

Funções Auxiliares: Há várias funções auxiliares, como:

exibir_nome_do_programa(): Exibe o nome do programa em formato ASCII.

exibir_opcoes(): Exibe as opções disponíveis no menu principal.

cadastrar_novo_restaurante(): Permite ao usuário cadastrar um novo restaurante.

listar_restaurantes(): Exibe a lista de todos os restaurantes cadastrados.

alternar_estado_restaurante(): Permite ao usuário alternar o estado de um restaurante específico.

voltar_ao_menu_principal(): Espera a entrada do usuário para voltar ao menu principal.

opcao_invalida(): Informa ao usuário que uma opção inválida foi escolhida.

Execução: O programa começa executando a função main().

***Como Usar***

Execute o programa.

O menu principal será exibido com as opções disponíveis.

Escolha uma opção digitando o número correspondente e pressione Enter:
Opção 1: Cadastrar um novo restaurante.

Opção 2: Listar os restaurantes cadastrados.

Opção 3: Alternar o estado de um restaurante específico.

Opção 4: Sair do programa.

Siga as instruções fornecidas para cada opção escolhida.

O programa continua executando até que você escolha a opção de sair.

***Considerações***

O sistema utiliza a biblioteca os para limpar a tela entre interações com o usuário. Isso melhora a experiência do usuário.
Certifique-se de que os restaurantes são inseridos com nomes corretos para evitar problemas na hora de alternar estados.
Esperamos que este README tenha sido útil para entender o funcionamento do sistema de gerenciamento de restaurantes. Sinta-se à vontade para modificar e adaptar o código conforme suas necessidades.
