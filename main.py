from Cadastro import adicionar_cadastro, editar_cadastro, excluir_cadastro, adicionar_estoque, remover_estoque, exibir_cadastros
from database import create_table

print('{:=^40}'.format(" Gerenciador de Estoque "))

# Menú de opções
def menu():
    while True:
        print('''
    ======== Menú =========
    [ 1 ] Adicionar produto
    [ 2 ] Editar produto
    [ 3 ] Excluir produto
    [ 4 ] Adicionar ao estoque 
    [ 5 ] Remover do estoque
    [ 6 ] Exibir cadastros
    [ 7 ] Sair
    ''')
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Nome do produto: ")
            cod = int(input("Código do produto: "))
            quantidade = int(input("Quantidade inicial: "))
            adicionar_cadastro(nome, cod, quantidade)

        elif opcao == '2':
            id = int(input("ID do produto a ser editado: "))
            nome = input("Novo nome do produto (deixe em branco para não alterar): ")
            cod = input("Novo código do produto (deixe em branco para não alterar): ")
            editar_cadastro(id, NomeProduto=nome if nome else None, Cod=int(cod) if cod else None)

        elif opcao == '3':
            id = int(input("ID do produto a ser excluído: "))
            excluir_cadastro(id)

        elif opcao == '4':
            id = int(input("ID do produto: "))
            quantidade = int(input("Quantidade a adicionar: "))
            adicionar_estoque(id, quantidade)

        elif opcao == '5':
            id = int(input("ID do produto: "))
            quantidade = int(input("Quantidade a remover: "))
            remover_estoque(id, quantidade)

        elif opcao == '6':
            exibir_cadastros()

        elif opcao == '7':
            print("Saindo do programa.")
            break

        else:
            print("Opção inválida. Tente novamente.")


# Teste rápido
create_table()
adicionar_cadastro('ProdutoTeste', 123, 10)
exibir_cadastros()

# Executando o menu interativo
menu()
