''' MARIA'''

from cliente import Cliente
from produto import Produto
from venda import Venda
from listaEncadeada import ListaEncadeada
from pilha import Pilha
from fila import Fila
from persistencia import (carregarClientes, salvarClientes, carregarProdutos, salvarProdutos, carregarVendas, salvarVendas)

class SistemaEstoque:
    def __init__(self):
        self.listaClientes = ListaEncadeada()
        self.listaProdutos = ListaEncadeada()
        self.filaVendas = Fila()
        self.historicoOperacoes = Pilha()

        carregarClientes(self.listaClientes)
        carregarProdutos(self.listaProdutos)
        carregarVendas(self.filaVendas, self.listaClientes, self.listaProdutos)

    def cadastrarCliente(self):
        print("\n===== CADASTRAR CLIENTE =====")
        idCliente = input("Digite o ID do cliente: ").strip()
        nomeCliente = input("Digite o nome do cliente: ").strip()

        if idCliente == "" or nomeCliente == "":
            print("Erro: ID e nome são obrigatórios.")
            return

        if self.listaClientes.buscarClientePorId(idCliente) is not None:
            print("Erro: o ID do cliente já existe.")
            return

        if self.listaClientes.buscarClientePorNome(nomeCliente) is not None:
            print("Erro: o nome do cliente já existe.")
            return

        cliente = Cliente(idCliente, nomeCliente)
        self.listaClientes.inserirFim(cliente)
        salvarClientes(self.listaClientes)

        self.historicoOperacoes.push(("cadastroCliente", cliente.idCliente))
        print("Cliente cadastrado com sucesso.")

    def listarClientes(self):
        print("\n===== LISTA DE CLIENTES =====")
        clientes = self.listaClientes.listar()

        if len(clientes) == 0:
            print("Nenhum cliente cadastrado.")
            return

        for cliente in clientes:
            print(cliente)

''' CAMILA'''

    def cadastrarProduto(self):
        print("\n===== CADASTRAR PRODUTO =====")
        idProduto = input("Digite o ID do produto: ").strip()
        nomeProduto = input("Digite o nome do produto: ").strip()

        if idProduto == "" or nomeProduto == "":
            print("Erro: ID e nome são obrigatórios.")
            return

        if self.listaProdutos.buscarProdutoPorId(idProduto) is not None:
            print("Erro: o ID do produto já existe.")
            return

        if self.listaProdutos.buscarProdutoPorNome(nomeProduto) is not None:
            print("Erro: o nome do produto já existe.")
            return

        try:
            quantidadeEstoque = int(input("Digite a quantidade em estoque: "))
            precoProduto = float(input("Digite o preço do produto: "))
        except:
            print("Erro: quantidade e preço devem ser numéricos.")
            return

        if quantidadeEstoque < 0:
            print("Erro: a quantidade não pode ser negativa.")
            return

        if precoProduto <= 0:
            print("Erro: o preço deve ser maior que zero.")
            return

        produto = Produto(idProduto, nomeProduto, quantidadeEstoque, precoProduto)
        self.listaProdutos.inserirFim(produto)
        salvarProdutos(self.listaProdutos)

        self.historicoOperacoes.push(("cadastroProduto", produto.idProduto))
        print("Produto cadastrado com sucesso.")

    def listarProdutos(self):
        print("\n===== LISTA DE PRODUTOS =====")
        produtos = self.listaProdutos.listar()

        if len(produtos) == 0:
            print("Nenhum produto cadastrado.")
            return

        for produto in produtos:
            print(produto)

    def pesquisarProduto(self):
        print("\n===== PESQUISAR PRODUTO =====")
        opcao = input("Pesquisar por 1-ID ou 2-Nome? ").strip()

        if opcao == "1":
            idProduto = input("Digite o ID do produto: ").strip()
            produto = self.listaProdutos.buscarProdutoPorId(idProduto)
        elif opcao == "2":
            nomeProduto = input("Digite o nome do produto: ").strip()
            produto = self.listaProdutos.buscarProdutoPorNome(nomeProduto)
        else:
            print("Opção inválida.")
            return

        if produto is None:
            print("Produto não encontrado.")
        else:
            print(produto)

''' EMILLY'''

    def realizarVenda(self):
        print("\n===== REALIZAR VENDA =====")
        idVenda = input("Digite o ID da venda: ").strip()
        idCliente = input("Digite o ID do cliente: ").strip()
        idProduto = input("Digite o ID do produto: ").strip()

        if idVenda == "" or idCliente == "" or idProduto == "":
            print("Erro: os IDs são obrigatórios.")
            return

        vendas = self.filaVendas.listar()
        for venda in vendas:
            if str(venda.idVenda) == str(idVenda):
                print("Erro: o ID da venda já existe.")
                return

        cliente = self.listaClientes.buscarClientePorId(idCliente)
        if cliente is None:
            print("Erro: cliente não encontrado.")
            return

        produto = self.listaProdutos.buscarProdutoPorId(idProduto)
        if produto is None:
            print("Erro: produto não encontrado.")
            return

        try:
            quantidade = int(input("Digite a quantidade vendida: "))
        except:
            print("Erro: a quantidade deve ser um número inteiro.")
            return

        if quantidade <= 0:
            print("Erro: a quantidade deve ser maior que zero.")
            return

        if quantidade > produto.quantidadeEstoque:
            print("Erro: estoque insuficiente.")
            return

        quantidadeAnterior = produto.quantidadeEstoque
        produto.quantidadeEstoque -= quantidade

        venda = Venda(idVenda, cliente, produto, quantidade)
        self.filaVendas.enqueue(venda)

        salvarProdutos(self.listaProdutos)
        salvarVendas(self.filaVendas)

        self.historicoOperacoes.push(("venda", venda.idVenda, produto.idProduto, quantidadeAnterior))
        print("Venda realizada com sucesso.")

    def visualizarFilaVendas(self):
        print("\n===== FILA DE VENDAS =====")
        vendas = self.filaVendas.listar()

        if len(vendas) == 0:
            print("Nenhuma venda registrada.")
            return

        for venda in vendas:
            print(venda)

    def desfazerUltimaOperacao(self):
        print("\n===== DESFAZER ÚLTIMA OPERAÇÃO =====")

        if self.historicoOperacoes.estaVazia():
            print("Não há operações para desfazer.")
            return

        operacao = self.historicoOperacoes.pop()

        if operacao[0] == "cadastroCliente":
            idCliente = operacao[1]
            clienteRemovido = self.listaClientes.removerClientePorId(idCliente)

            if clienteRemovido is not None:
                salvarClientes(self.listaClientes)
                print("Cadastro de cliente desfeito com sucesso.")
            else:
                print("Não foi possível desfazer o cadastro do cliente.")

        elif operacao[0] == "cadastroProduto":
            idProduto = operacao[1]
            produtoRemovido = self.listaProdutos.removerProdutoPorId(idProduto)

            if produtoRemovido is not None:
                salvarProdutos(self.listaProdutos)
                print("Cadastro de produto desfeito com sucesso.")
            else:
                print("Não foi possível desfazer o cadastro do produto.")

        elif operacao[0] == "venda":
            idVenda = operacao[1]
            idProduto = operacao[2]
            quantidadeAnterior = operacao[3]

            vendas = self.filaVendas.listar()
            indiceVenda = -1

            for i in range(len(vendas)):
                if str(vendas[i].idVenda) == str(idVenda):
                    indiceVenda = i

            if indiceVenda != -1:
                vendas.pop(indiceVenda)

                produto = self.listaProdutos.buscarProdutoPorId(idProduto)
                if produto is not None:
                    produto.quantidadeEstoque = quantidadeAnterior

                salvarProdutos(self.listaProdutos)
                salvarVendas(self.filaVendas)
                print("Venda desfeita com sucesso.")
            else:
                print("Não foi possível desfazer a venda.")

        else:
            print("Operação desconhecida.")

    def exibirValorTotalEstoque(self):
        print("\n===== VALOR TOTAL DO ESTOQUE =====")
        totalEstoque = 0

        for produto in self.listaProdutos.listar():
            totalEstoque += produto.quantidadeEstoque * produto.precoProduto

        print(f"Valor total do estoque: R${totalEstoque:.2f}")

    def exibirValorTotalVendas(self):
        print("\n===== VALOR TOTAL DE VENDAS =====")
        totalVendas = 0

        for venda in self.filaVendas.listar():
            totalVendas += venda.valorTotal

        print(f"Valor total de vendas: R${totalVendas:.2f}")

    def exibirClientesEValoresGastos(self):
        print("\n===== CLIENTES E VALORES GASTOS =====")

        clientes = self.listaClientes.listar()
        vendas = self.filaVendas.listar()

        if len(clientes) == 0:
            print("Nenhum cliente cadastrado.")
            return

        for cliente in clientes:
            totalGasto = 0

            for venda in vendas:
                if str(venda.cliente.idCliente) == str(cliente.idCliente):
                    totalGasto += venda.valorTotal

            print(f"Cliente: {cliente.nomeCliente} | Total gasto: R${totalGasto:.2f}")
