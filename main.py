from estoque import SistemaEstoque

def exibir_menu():
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
    sistema = SistemaEstoque()

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            sistema.cadastrar_cliente()

        elif opcao == "2":
            sistema.listar_clientes()

        elif opcao == "3":
            sistema.cadastrar_produto()

        elif opcao == "4":
            sistema.listar_produtos()

        elif opcao == "5":
            sistema.pesquisar_produto()

        elif opcao == "6":
            sistema.realizar_venda()

        elif opcao == "7":
            sistema.visualizar_fila_vendas()

        elif opcao == "8":
            sistema.desfazer_ultima_operacao()

        elif opcao == "9":
            sistema.exibir_valor_total_estoque()

        elif opcao == "10":
            sistema.exibir_valor_total_vendas()

        elif opcao == "11":
            sistema.exibir_clientes_valores_gastos()

        elif opcao == "12":
            print("Encerrando o sistema...")
            break

        else:
            print("Opção inválida. Tente novamente.")


main()