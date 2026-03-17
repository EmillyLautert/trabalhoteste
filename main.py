'''MATHIAS'''

from estoque import SistemaEstoque


def exibirMenu():
    print("\n===== MENU DO SISTEMA =====")
    print("1 - Cadastrar cliente")
    print("2 - Listar clientes")
    print("3 - Cadastrar produto")
    print("4 - Listar produtos")
    print("5 - Pesquisar produto")
    print("6 - Realizar venda")
    print("7 - Visualizar fila de vendas")
    print("8 - Desfazer última operação")
    print("9 - Exibir valor total do estoque")
    print("10 - Exibir valor total de vendas")
    print("11 - Exibir clientes e valores gastos")
    print("12 - Sair")


def main():
    sistema = SistemaEstoque()

    while True:
        exibirMenu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            sistema.cadastrarCliente()
        elif opcao == "2":
            sistema.listarClientes()
        elif opcao == "3":
            sistema.cadastrarProduto()
        elif opcao == "4":
            sistema.listarProdutos()
        elif opcao == "5":
            sistema.pesquisarProduto()
        elif opcao == "6":
            sistema.realizarVenda()
        elif opcao == "7":
            sistema.visualizarFilaVendas()
        elif opcao == "8":
            sistema.desfazerUltimaOperacao()
        elif opcao == "9":
            sistema.exibirValorTotalEstoque()
        elif opcao == "10":
            sistema.exibirValorTotalVendas()
        elif opcao == "11":
            sistema.exibirClientesEValoresGastos()
        elif opcao == "12":
            print("Sistema encerrado.")
            break
        else:
            print("Opção inválida.")


main()
