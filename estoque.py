from cliente import Cliente
from produto import Produto
from venda import Venda
from listaEncadeada import ListaEncadeada
from pilha import Pilha
from fila import Fila
from persistencia import carregar_clientes, salvar_clientes, carregar_produtos, salvar_produtos, carregar_vendas, salvar_vendas

class SistemaEstoque:
    def __init__(self):
        self.clientes = ListaEncadeada()
        self.produtos = ListaEncadeada()
        self.vendas = Fila()
        self.historico = Pilha()

        carregar_clientes(self.clientes)
        carregar_produtos(self.produtos)
        carregar_vendas(self.vendas, self.clientes, self.produtos)

    def cadastrar_cliente(self):
        print("\n===== CADASTRAR CLIENTE =====")

        id_cliente = input("Digite o ID do cliente: ").strip()
        nome = input("Digite o nome do cliente: ").strip()

        if id_cliente == "" or nome == "":
            print("Erro: ID e nome são obrigatórios.")
            return

        # verificar ID duplicado
        if self.clientes.buscar_por_id(id_cliente) is not None:
            print("Erro: já existe um cliente com esse ID.")
            return

        # verificar nome duplicado
        if self.clientes.buscar_por_nome(nome) is not None:
            print("Erro: já existe um cliente com esse nome.")
            return

        cliente = Cliente(id_cliente, nome)

        self.clientes.inserir_fim(cliente)
        salvar_clientes(self.clientes)

        self.historico.push(("cadastro_cliente", cliente.id))

        print("Cliente cadastrado com sucesso.")

    def listar_clientes(self):
        print("\n===== LISTA DE CLIENTES =====")
        lista = self.clientes.listar()

        if len(lista) == 0:
            print("Nenhum cliente cadastrado.")
            return

        for cliente in lista:
            print(cliente)
            
'''MARIA ATÉ AQUI E DEPOIS CAMILA'''

    def cadastrar_produto(self):
        print("\n===== CADASTRAR PRODUTO =====")

        id_produto = input("Digite o ID do produto: ").strip()
        nome = input("Digite o nome do produto: ").strip()

        if id_produto == "" or nome == "":
            print("Erro: ID e nome são obrigatórios.")
            return

        # verificar ID duplicado
        if self.produtos.buscar_por_id(id_produto) is not None:
            print("Erro: já existe um produto com esse ID.")
            return

        # verificar nome duplicado
        if self.produtos.buscar_por_nome(nome) is not None:
            print("Erro: já existe um produto com esse nome.")
            return

        try:
            quantidade = int(input("Digite a quantidade: "))
            preco = float(input("Digite o preço: "))
        except:
            print("Erro: quantidade e preço devem ser números inteiros sem vírgula.")
            return

        if quantidade < 0:
            print("Erro: quantidade não pode ser negativa.")
            return

        if preco <= 0:
            print("Erro: preço deve ser maior que zero.")
            return

        produto = Produto(id_produto, nome, quantidade, preco)

        self.produtos.inserir_fim(produto)
        salvar_produtos(self.produtos)

        self.historico.push(("cadastro_produto", produto.id))

        print("Produto cadastrado com sucesso.")

    def listar_produtos(self):
        print("\n===== LISTA DE PRODUTOS =====")
        lista = self.produtos.listar()

        if len(lista) == 0:
            print("Nenhum produto cadastrado.")
            return

        for produto in lista:
            print(produto)

    def pesquisar_produto(self):
        print("\n===== PESQUISAR PRODUTO =====")
        opcao = input("Pesquisar por 1-ID ou 2-Nome? ").strip()

        if opcao == "1":
            id_produto = input("Digite o ID: ").strip()
            produto = self.produtos.buscar_por_id(id_produto)

        elif opcao == "2":
            nome = input("Digite o nome: ").strip()
            produto = self.produtos.buscar_por_nome(nome)

        else:
            print("Opção inválida.")
            return

        if produto is None:
            print("Produto não encontrado.")
        else:
            print(produto)
            
'''ATÉ AQUI CAMILA E DEPOIS EMILLY'''

    def realizar_venda(self):
        print("\n===== REALIZAR VENDA =====")
        id_venda = input("Digite o ID da venda: ").strip()
        id_cliente = input("Digite o ID do cliente: ").strip()
        id_produto = input("Digite o ID do produto: ").strip()

        if id_venda == "" or id_cliente == "" or id_produto == "":
            print("Erro: IDs não podem ser vazios.")
            return

        cliente = self.clientes.buscar_por_id(id_cliente)
        if cliente is None:
            print("Erro: cliente não cadastrado.")
            return

        produto = self.produtos.buscar_por_id(id_produto)
        if produto is None:
            print("Erro: produto não cadastrado.")
            return

        try:
            quantidade = int(input("Digite a quantidade vendida: "))
        except:
            print("Erro: a quantidade deve ser um número inteiro.")
            return

        if quantidade <= 0:
            print("Erro: a quantidade deve ser maior que zero.")
            return

        if quantidade > produto.quantidade:
            print("Erro: estoque insuficiente.")
            return

        valor_total = quantidade * produto.preco
        venda = Venda(id_venda, cliente, produto, quantidade, valor_total)

        quantidade_anterior = produto.quantidade
        produto.quantidade -= quantidade

        self.vendas.enqueue(venda)

        salvar_produtos(self.produtos)
        salvar_vendas(self.vendas)

        self.historico.push(("venda", venda.id, produto.id, quantidade_anterior))
        print("Venda realizada com sucesso.")

    def visualizar_fila_vendas(self):
        print("\n===== FILA DE VENDAS =====")
        lista = self.vendas.listar()

        if len(lista) == 0:
            print("Nenhuma venda registrada.")
            return

        for venda in lista:
            print(venda)

    def desfazer_ultima_operacao(self):
        print("\n===== DESFAZER ÚLTIMA OPERAÇÃO =====")

        if self.historico.esta_vazia():
            print("Não há operações para desfazer.")
            return

        operacao = self.historico.pop()

        if operacao[0] == "cadastro_cliente":
            id_cliente = operacao[1]
            removido = self.clientes.remover_por_id(id_cliente)
            if removido is not None:
                salvar_clientes(self.clientes)
                print("Último cadastro de cliente desfeito.")
            else:
                print("Não foi possível desfazer a operação.")

        elif operacao[0] == "cadastro_produto":
            id_produto = operacao[1]
            removido = self.produtos.remover_por_id(id_produto)
            if removido is not None:
                salvar_produtos(self.produtos)
                print("Último cadastro de produto desfeito.")
            else:
                print("Não foi possível desfazer a operação.")

        elif operacao[0] == "venda":
            id_venda = operacao[1]
            id_produto = operacao[2]
            quantidade_anterior = operacao[3]

            lista_vendas = self.vendas.listar()
            indice = -1

            for i in range(len(lista_vendas)):
                if lista_vendas[i].id == id_venda:
                    indice = i

            if indice != -1:
                lista_vendas.pop(indice)

                produto = self.produtos.buscar_por_id(id_produto)
                if produto is not None:
                    produto.quantidade = quantidade_anterior

                salvar_produtos(self.produtos)
                salvar_vendas(self.vendas)
                print("Última venda desfeita com sucesso.")
            else:
                print("Não foi possível desfazer a venda.")

        else:
            print("Operação desconhecida.")

    def exibir_valor_total_estoque(self):
        print("\n===== VALOR TOTAL DO ESTOQUE =====")
        total = 0

        for produto in self.produtos.listar():
            total += produto.quantidade * produto.preco

        print(f"Valor total do estoque: R$ {total:.2f}")

    def exibir_valor_total_vendas(self):
        print("\n===== VALOR TOTAL DE VENDAS =====")
        total = 0

        for venda in self.vendas.listar():
            total += venda.valor_total

        print(f"Valor total vendido: R$ {total:.2f}")

    def exibir_clientes_valores_gastos(self):
        print("\n===== CLIENTES E VALORES GASTOS =====")

        lista_clientes = self.clientes.listar()
        lista_vendas = self.vendas.listar()

        if len(lista_clientes) == 0:
            print("Nenhum cliente cadastrado.")
            return

        for cliente in lista_clientes:
            total_gasto = 0

            for venda in lista_vendas:
                if venda.cliente.id == cliente.id:
                    total_gasto += venda.valor_total

            print(f"Cliente: {cliente.nome} | Total gasto: R$ {total_gasto:.2f}")
