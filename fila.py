''' GABI'''

class Fila:
    def __init__(self):
        self.itens = []

    def enqueue(self, item):
        self.itens.append(item)

    def dequeue(self):
        if self.estaVazia():
            return None
        return self.itens.pop(0)

    def front(self):
        if self.estaVazia():
            return None
        return self.itens[0]

    def listar(self):
        return self.itens

    def estaVazia(self):
        return len(self.itens) == 0

    def tamanho(self):
        return len(self.itens)
