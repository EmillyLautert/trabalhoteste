from cliente import Cliente
from produto import Produto
from venda import Venda
from listaEncadeada import ListaEncadeada
from pilha import Pilha
from fila import Fila
from persistencia import carregarClientes, salvarClientes, carregarProdutos, salvarProdutos, carregarVendas, salvarVendas

class SistemaEstoque:
    def __init__(self):
        self.clientes = ListaEncadeada()
        self.produtos = ListaEncadeada()
        self.vendas = Fila()
        self.historico = Pilha()

        carregarClientes(self.clientes)
        carregarProdutos(self.produtos)
        carregarVendas(self.vendas, self.clientes, self.produtos)

    def cadastrarCliente(self):
        print("\n===== CADASTRAR CLIENTE =====")

        idCliente = input("Digite o ID do cliente: ").strip()
        nomeCliente = input("Digite o nome do cliente: ").strip()

        if idCliente == "" or nomeCliente == "":
            print("Erro: ID e nome são obrigatórios.")
            return

        # verificar ID duplicado
        if self.clientes.buscarIdCliente (idCliente) is not None:
            print("Erro: já existe um cliente com esse ID.")
            return

        # verificar nome duplicado
        if self.clientes.buscarNomeCliente (nomeCliente) is not None:
            print("Erro: já existe um cliente com esse nome.")
            return

        cliente = Cliente(idCliente, nomeCliente)

        self.clientes.inserirFim(cliente)
        salvarClientes(self.clientes)

        self.historico.push(("cadastroCliente", cliente.idCliente))

        print("Cliente cadastrado com sucesso.")

    def listarClientes(self):
        print("\n===== LISTA DE CLIENTES =====")
        lista = self.clientes.listar()

        if len(lista) == 0:
            print("Nenhum cliente cadastrado.")
            return

        for cliente in lista:
            print(cliente)
            
'''MARIA ATÉ AQUI E DEPOIS CAMILA'''

    def cadastrarProduto(self):
        print("\n===== CADASTRAR PRODUTO =====")

        idProduto = input("Digite o ID do produto: ").strip()
        nomeProduto = input("Digite o nome do produto: ").strip()

        if idProduto == "" or nomeProduto == "":
            print("Erro: ID e nome são obrigatórios.")
            return

        # verificar ID duplicado
        if self.produtos.buscarIdProduto(idProduto) is not None:
            print("Erro: já existe um produto com esse ID.")
            return

        # verificar nome duplicado
        if self.produtos.buscarNomeProduto(nomeProduto) is not None:
            print("Erro: já existe um produto com esse nome.")
            return

        try:
            quantidadeProduto = int(input("Digite a quantidade: "))
            precoProduto = float(input("Digite o preço: "))
        except:
            print("Erro: quantidade e preço devem ser números inteiros sem vírgula.")
            return

        if quantidadeProduto < 0:
            print("Erro: quantidade não pode ser negativa.")
            return

        if precoProduto <= 0:
            print("Erro: preço deve ser maior que zero.")
            return

        produto = Produto(idProduto, nomeProduto, quantidadeProduto, precoProduto)

        self.produtos.inserirFim(produto)
        salvarProdutos(self.produtos)

        self.historico.push(("cadastroProduto", produto.idProduto))

        print("Produto cadastrado com sucesso.")

    def listarProdutos(self):
        print("\n===== LISTA DE PRODUTOS =====")
        lista = self.produtos.listar()

        if len(lista) == 0:
            print("Nenhum produto cadastrado.")
            return

        for produto in lista:
            print(produto)

    def pesquisarProduto(self):
        print("\n===== PESQUISAR PRODUTO =====")
        opcao = input("Pesquisar por 1-ID ou 2-Nome? ").strip()

        if opcao == "1":
            idProduto = input("Digite o ID: ").strip()
            produto = self.produtos.buscarIdProduto(idProduto)

        elif opcao == "2":
            nomeProduto = input("Digite o nome: ").strip()
            produto = self.produtos.buscarNomeProduto(nomeProduto)

        else:
            print("Opção inválida.")
            return

        if produto is None:
            print("Produto não encontrado.")
        else:
            print(produto)
            
'''ATÉ AQUI CAMILA E DEPOIS EMILLY'''

    def realizarVenda(self):
        print("\n===== REALIZAR VENDA =====")
        idVenda = input("Digite o ID da venda: ").strip()
        idCliente = input("Digite o ID do cliente: ").strip()
        idProduto = input("Digite o ID do produto: ").strip()

        if idVenda == "" or idCliente == "" or idProduto == "":
            print("Erro: IDs não podem ser vazios.")
            return

        cliente = self.clientes.buscarIdCliente(idCliente)
        if cliente is None:
            print("Erro: cliente não cadastrado.")
            return

        produto = self.produtos.buscarIdProduto(idProduto)
        if produto is None:
            print("Erro: produto não cadastrado.")
            return

        try:
            quantidadeVenda = int(input("Digite a quantidade vendida: "))
        except:
            print("Erro: a quantidade deve ser um número inteiro.")
            return

        if quantidadeVenda <= 0:
            print("Erro: a quantidade deve ser maior que zero.")
            return

        elif quantidadeVenda > produto.quantidadeProduto:
            print("Erro: estoque insuficiente.")
            return
        else    
            valorTotal = quantidadeVenda * produto.precoProduto
            venda = Venda(idVenda, cliente, produto, quantidadeVenda, valorTotal)

            quantidadeAnterior = produto.quantidadeProduto
            produto.quantidadeProduto -= quantidadeVenda

            self.vendas.enqueue(venda)

            salvarProdutos(self.produtos)
            salvarVendas(self.vendas)

            self.historico.push(("venda", venda.idVenda, produto.idProduto, quantidadeAnterior))
            print("Venda realizada com sucesso.")

    def visualizarFilaVendas(self):
        print("\n===== FILA DE VENDAS =====")
        lista = self.vendas.listar()

        if len(lista) == 0:
            print("Nenhuma venda registrada.")
            return

        for venda in lista:
            print(venda)

    def desfazerUltimaOperacao(self):
        print("\n===== DESFAZER ÚLTIMA OPERAÇÃO =====")

        if self.historico.estaVazia():
            print("Não há operações para desfazer.")
            return

        operacao = self.historico.pop()

        if operacao[0] == "cadastroCliente":
            idCliente = operacao[1]
            removido = self.clientes.removerIdCliente(idCliente)
            if removido is not None:
                salvarClientes(self.clientes)
                print("Último cadastro de cliente desfeito.")
            else:
                print("Não foi possível desfazer a operação.")

        elif operacao[0] == "cadastroProduto":
            idProduto = operacao[1]
            removido = self.produtos.removerIdProduto(idProduto)
            if removido is not None:
                salvarProdutos(self.produtos)
                print("Último cadastro de produto desfeito.")
            else:
                print("Não foi possível desfazer a operação.")

        elif operacao[0] == "venda":
            idVenda = operacao[1]
            idProduto = operacao[2]
            quantidadeAnterior = operacao[3]

            listaVendas = self.vendas.listar()
            indice = -1

            for i in range(len(listaVendas)):
                if listaVendas[i].id == idVenda:
                    indice = i

            if indice != -1:
                listaVendas.pop(indice)

                produto = self.produtos.buscarIdProduto(idProduto)
                if produto is not None:
                    produto.quantidadeProduto = quantidadeAnterior

                salvarProdutos(self.produtos)
                salvarVendas(self.vendas)
                print("Última venda desfeita com sucesso.")
            else:
                print("Não foi possível desfazer a venda.")

        else:
            print("Operação desconhecida.")

    def valorTotalEstoque(self):
        print("\n===== VALOR TOTAL DO ESTOQUE =====")
        total = 0

        for produto in self.produtos.listar():
            total += produto.quantidadeProduto * produto.precoProduto

        print(f"Valor total do estoque: R$ {total:.2f}")

    def valorTotalVendas(self):
        print("\n===== VALOR TOTAL DE VENDAS =====")
        total = 0

        for venda in self.vendas.listar():
            total += venda.valorTotal

        print(f"Valor total vendido: R$ {total:.2f}")

    def clientesValoresGastos(self):
        print("\n===== CLIENTES E VALORES GASTOS =====")

        listaClientes = self.clientes.listar()
        listaVendas = self.vendas.listar()

        if len(listaClientes) == 0:
            print("Nenhum cliente cadastrado.")
            return

        for cliente in listaClientes:
            totalGasto = 0

            for venda in listaVendas:
                if venda.cliente.id == cliente.id:
                    totalGasto += venda.valorTotal

            print(f"Cliente: {cliente.nomeCliente} | Total gasto: R$ {totalGasto:.2f}")
