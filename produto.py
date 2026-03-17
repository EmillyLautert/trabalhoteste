class Produto:
    """Representa um produto disponível no estoque."""

    def __init__(self, idProduto, nomeProduto, quantidadeEstoque, precoProduto):
        self.idProduto = idProduto
        self.nomeProduto = nomeProduto
        self.quantidadeEstoque = quantidadeEstoque
        self.precoProduto = precoProduto

    def __str__(self):
        return f"ID: {self.idProduto}, Nome: {self.nomeProduto}, Quantidade: {self.quantidadeEstoque}, Preço: R${self.precoProduto:.2f}"

    def to_csv(self):
        return f"{self.idProduto},{self.nomeProduto},{self.quantidadeEstoque},{self.precoProduto}\n"
