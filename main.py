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
            estoque.cadastrar_cliente()

        elif opcao == "2":
            estoque.listar_clientes()

        elif opcao == "3":
            estoque.cadastrar_produto()

        elif opcao == "4":
            estoque.listar_produtos()

        elif opcao == "5":
            estoque.pesquisar_produto()

        elif opcao == "6":
            estoque.realizar_venda()

        elif opcao == "7":
            estoque.visualizar_fila_vendas()

        elif opcao == "8":
            estoque.desfazer_ultima_operacao()

        elif opcao == "9":
            estoque.exibir_valor_total_estoque()

        elif opcao == "10":
            estoque.exibir_valor_total_vendas()

        elif opcao == "11":
            estoque.exibir_clientes_valores_gastos()

        elif opcao == "12":
            print("Encerrando o sistema...")
            break

        else:
            print("Opção inválida. Tente novamente.")


main()
