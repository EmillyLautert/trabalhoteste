import os
from cliente import Cliente
from produto import Produto
from venda import Venda


def garantir_arquivo(nome_arquivo):
    if not os.path.exists(nome_arquivo):
        with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
            pass


def carregar_clientes(lista_clientes):
    garantir_arquivo("clientes.csv")

    try:
        with open("clientes.csv", "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                linha = linha.strip()
                if linha == "":
                    continue

                partes = linha.split(";")
                if len(partes) != 2:
                    continue

                id_cliente = partes[0]
                nome = partes[1]

                if lista_clientes.buscar_por_id(id_cliente) is None:
                    cliente = Cliente(id_cliente, nome)
                    lista_clientes.inserir_fim(cliente)
    except:
        print("Erro ao carregar clientes. Tente novamente.")


def salvar_clientes(lista_clientes):
    try:
        with open("clientes.csv", "w", encoding="utf-8") as arquivo:
            for cliente in lista_clientes.listar():
                arquivo.write(cliente.to_csv() + "\n")
    except:
        print("Erro ao salvar clientes. Tente novamente.")


def carregar_produtos(lista_produtos):
    garantir_arquivo("produtos.csv")

    try:
        with open("produtos.csv", "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                linha = linha.strip()
                if linha == "":
                    continue

                partes = linha.split(";")
                if len(partes) != 4:
                    continue

                id_produto = partes[0]
                nome = partes[1]

                try:
                    quantidade = int(partes[2])
                    preco = float(partes[3])
                except:
                    continue

                if lista_produtos.buscar_por_id(id_produto) is None:
                    produto = Produto(id_produto, nome, quantidade, preco)
                    lista_produtos.inserir_fim(produto)
    except:
        print("Erro ao carregar produtos. Tente novamente.")


def salvar_produtos(lista_produtos):
    try:
        with open("produtos.csv", "w", encoding="utf-8") as arquivo:
            for produto in lista_produtos.listar():
                arquivo.write(produto.to_csv() + "\n")
    except:
        print("Erro ao salvar produtos. Tente novamente.")


def carregar_vendas(fila_vendas, lista_clientes, lista_produtos):
    garantir_arquivo("vendas.csv")

    try:
        with open("vendas.csv", "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                linha = linha.strip()
                if linha == "":
                    continue

                partes = linha.split(";")
                if len(partes) != 5:
                    continue

                id_venda = partes[0]
                id_cliente = partes[1]
                id_produto = partes[2]

                try:
                    quantidade = int(partes[3])
                    valor_total = float(partes[4])
                except:
                    continue

                cliente = lista_clientes.buscar_por_id(id_cliente)
                produto = lista_produtos.buscar_por_id(id_produto)

                if cliente is not None and produto is not None:
                    venda = Venda(id_venda, cliente, produto, quantidade, valor_total)
                    fila_vendas.enqueue(venda)
    except:
        print("Erro ao carregar vendas. Tente novamente.")


def salvar_vendas(fila_vendas):
    try:
        with open("vendas.csv", "w", encoding="utf-8") as arquivo:
            for venda in fila_vendas.listar():
                arquivo.write(venda.to_csv() + "\n")
    except:
        print("Erro ao salvar vendas. Tente novamente.")