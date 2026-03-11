class Venda:
    def __init__(self, id, cliente, produto, quantidade, valor_total):
        self.id = id
        self.cliente = cliente
        self.produto = produto
        self.quantidade = quantidade
        self.valor_total = valor_total

    def to_csv(self):
        return f"{self.id};{self.cliente.id};{self.produto.id};{self.quantidade};{self.valor_total}"

    def __str__(self):
        return (
            f"ID Venda: {self.id} | Cliente: {self.cliente.nome} | "
            f"Produto: {self.produto.nome} | Quantidade: {self.quantidade} | "
            f"Total: R$ {self.valor_total:.2f}"
        )