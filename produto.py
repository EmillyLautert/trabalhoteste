class Produto:
    def __init__(self, idProduto, nomeProduto, quantidadeProduto, precoProduto):
        self.idProduto = idProduto
        self.nomeProduto = nomeProduto
        self.quantidadeProduto = quantidadeProduto
        self.precoProduto = precoProduto

    def to_csv(self):
        return f"{self.idProduto};{self.nomeProduto};{self.quantidadeProduto};{self.precoProduto}"

    def __str__(self):
        return f"ID: {self.idProduto} | Nome: {self.nomeProduto} | Qtd: {self.quantidadeProduto} | Preço: R$ {self.precoProduto:.2f}"
