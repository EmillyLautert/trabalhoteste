class Cliente:
    def __init__(self, id, nome):
        self.idCliente = idCliente
        self.nomeCliente = nomeCliente

    def to_csv(self):
        return f"{self.idCliente};{self.nomeCliente}"

    def __str__(self):
        return f"ID: {self.idCliente} | Nome: {self.nomeCliente}"
