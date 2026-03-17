''' GABI '''

import os
from cliente import Cliente
from produto import Produto
from venda import Venda


def garantirArquivo(nomeArquivo):
    if not os.path.exists(nomeArquivo):
        with open(nomeArquivo, "w", encoding="utf-8") as arquivo:
            pass


def carregarClientes(listaClientes):
    garantirArquivo("clientes.csv")

    try:
        with open("clientes.csv", "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                linha = linha.strip()

                if linha == "":
                    continue

                partes = linha.split(",")

                if len(partes) != 2:
                    continue

                idCliente = partes[0]
                nomeCliente = partes[1]

                if listaClientes.buscarClientePorId(idCliente) is None:
                    cliente = Cliente(idCliente, nomeCliente)
                    listaClientes.inserirFim(cliente)
    except:
        print("Erro ao carregar clientes.")


def salvarClientes(listaClientes):
    try:
        with open("clientes.csv", "w", encoding="utf-8") as arquivo:
            for cliente in listaClientes.listar():
                arquivo.write(cliente.to_csv())
    except:
        print("Erro ao salvar clientes.")


def carregarProdutos(listaProdutos):
    garantirArquivo("produtos.csv")

    try:
        with open("produtos.csv", "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                linha = linha.strip()

                if linha == "":
                    continue

                partes = linha.split(",")

                if len(partes) != 4:
                    continue

                idProduto = partes[0]
                nomeProduto = partes[1]

                try:
                    quantidadeEstoque = int(partes[2])
                    precoProduto = float(partes[3])
                except:
                    continue

                if listaProdutos.buscarProdutoPorId(idProduto) is None:
                    produto = Produto(idProduto, nomeProduto, quantidadeEstoque, precoProduto)
                    listaProdutos.inserirFim(produto)
    except:
        print("Erro ao carregar produtos.")


def salvarProdutos(listaProdutos):
    try:
        with open("produtos.csv", "w", encoding="utf-8") as arquivo:
            for produto in listaProdutos.listar():
                arquivo.write(produto.to_csv())
    except:
        print("Erro ao salvar produtos.")

''' MATHIAS '''

def carregarVendas(filaVendas, listaClientes, listaProdutos):
    garantirArquivo("vendas.csv")

    try:
        with open("vendas.csv", "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                linha = linha.strip()

                if linha == "":
                    continue

                partes = linha.split(",")

                if len(partes) != 5:
                    continue

                idVenda = partes[0]
                idCliente = partes[1]
                idProduto = partes[2]

                try:
                    quantidade = int(partes[3])
                except:
                    continue

                cliente = listaClientes.buscarClientePorId(idCliente)
                produto = listaProdutos.buscarProdutoPorId(idProduto)

                if cliente is not None and produto is not None:
                    venda = Venda(idVenda, cliente, produto, quantidade)
                    filaVendas.enqueue(venda)
    except:
        print("Erro ao carregar vendas.")


def salvarVendas(filaVendas):
    try:
        with open("vendas.csv", "w", encoding="utf-8") as arquivo:
            for venda in filaVendas.listar():
                arquivo.write(venda.to_csv())
    except:
        print("Erro ao salvar vendas.")
