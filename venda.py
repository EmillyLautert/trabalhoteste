class Venda:
    def __init__(self, idVenda, clienteVenda, produtoVenda, quantidadeVenda, valorTotal):
        self.idVenda = idVenda
        self.clienteVenda = clienteVenda
        self.produtoVenda = produtoVenda
        self.quantidadeVenda = quantidadeVenda
        self.valorTotal = valorTotal

    def to_csv(self):
        return f"{self.idVenda};{self.cliente.idCliente};{self.produto.idProduto};{self.quantidadeVenda};{self.valorTotal}"

    def __str__(self):
        return (
            f"ID Venda: {self.idVenda} | Cliente: {self.cliente.nomeCliente} | "
            f"Produto: {self.produto.nomeProduto} | Quantidade: {self.quantidadeVenda} | "
            f"Total: R$ {self.valorTotal:.2f}"
        )
