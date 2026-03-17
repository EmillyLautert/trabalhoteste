'''MARIA'''

class Pilha:
    def __init__(self):
        self.itens = []

    def push(self, item):
        self.itens.append(item)

    def pop(self):
        if self.estaVazia():
            return None
        return self.itens.pop()

    def peek(self):
        if self.estaVazia():
            return None
        return self.itens[-1]

    def estaVazia(self):
        return len(self.itens) == 0

    def tamanho(self):
        return len(self.itens)
