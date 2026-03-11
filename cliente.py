class Cliente:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome

    def to_csv(self):
        return f"{self.id};{self.nome}"

    def __str__(self):
        return f"ID: {self.id} | Nome: {self.nome}"