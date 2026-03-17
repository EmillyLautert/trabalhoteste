'''MATHIAS AQUI'''

from estoque import SistemaEstoque

def menu():
    print("\n===== MENU ESTOQUE =====")
    print("1 - Cadastrar cliente")
    print("2 - Listar clientes")
    print("3 - Cadastrar produto")
    print("4 - Listar produtos")
    print("5 - Pesquisar produto")
    print("6 - Realizar venda")
    print("7 - Ver fila de vendas")
    print("8 - Desfazer última operação")
    print("9 - Exibir valor total do estoque")
    print("10 - Exibir valor total de vendas")
    print("11 - Exibir clientes e valores gastos")
    print("12 - Sair")
    print("========================")


def main():
    estoque = SistemaEstoque()

    while True:
        menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            estoque.cadastrarCliente()

        elif opcao == "2":
            estoque.listarClientes()

        elif opcao == "3":
            estoque.cadastrarProduto()

        elif opcao == "4":
            estoque.listarProdutos()

        elif opcao == "5":
            estoque.pesquisarProduto()

        elif opcao == "6":
            estoque.realizarVenda()

        elif opcao == "7":
            estoque.visualizarFilaVendas()

        elif opcao == "8":
            estoque.desfazerUltimaOperacao()

        elif opcao == "9":
            estoque.valorTotalEstoque()

        elif opcao == "10":
            estoque.valorTotalVendas()

        elif opcao == "11":
            estoque.clientesValoresGastos()

        elif opcao == "12":
            print("Encerrando o sistema...")
            break

        else:
            print("Opção inválida. Tente novamente.")


main()
