class Venda:
    """Representa uma venda realizada no sistema."""

    def __init__(self, idVenda, cliente, produto, quantidade):
        self.idVenda = idVenda
        self.cliente = cliente
        self.produto = produto
        self.quantidade = quantidade
        self.valorTotal = quantidade * produto.precoProduto

    def __str__(self):
        return f"ID: {self.idVenda}, Cliente: {self.cliente.nomeCliente}, Produto: {self.produto.nomeProduto}, Quantidade: {self.quantidade}, Valor Total: R${self.valorTotal:.2f}"

    def to_csv(self):
        return f"{self.idVenda},{self.cliente.idCliente},{self.produto.idProduto},{self.quantidade},{self.valorTotal}\n"
