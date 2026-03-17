class Cliente:
    """Representa um cliente cadastrado no sistema."""

    def __init__(self, idCliente, nomeCliente):
        self.idCliente = idCliente
        self.nomeCliente = nomeCliente

    def __str__(self):
        return f"ID: {self.idCliente}, Nome: {self.nomeCliente}"

    def to_csv(self):
        return f"{self.idCliente},{self.nomeCliente}\n"
