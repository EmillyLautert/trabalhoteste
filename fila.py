class Fila:
    def __init__(self):
        self._itens = []

    def enqueue(self, item):
        self._itens.append(item)

    def dequeue(self):
        if self.esta_vazia():
            return None
        return self._itens.pop(0)

    def front(self):
        if self.estaVazia():
            return None
        return self._itens[0]

    def estaVazia(self):
        return len(self._itens) == 0

    def listar(self):
        return self._itens

    def tamanho(self):
        return len(self._itens)
