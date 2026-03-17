class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None


class ListaEncadeada:
    def __init__(self):
        self.head = None

    def inserirFim(self, valor):
        novo = Nodo(valor)

        if self.head is None:
            self.head = novo
            return

        atual = self.head
        while atual.proximo is not None:
            atual = atual.proximo

        atual.proximo = novo

    def listar(self):
        elementos = []
        atual = self.head

        while atual is not None:
            elementos.append(atual.valor)
            atual = atual.proximo

        return elementos

    def buscarIdProduto(self, idProduto):
        atual = self.head

        while atual is not None:
            if str(atual.valor.id) == str(id):
                return atual.valor
            atual = atual.proximo

        return None

    def buscarIdCliente(self, idCliente):
        atual = self.head

        while atual is not None:
            if str(atual.valor.id) == str(id):
                return atual.valor
            atual = atual.proximo

        return None

    def buscarIdVenda(self, idVenda):
        atual = self.head

        while atual is not None:
            if str(atual.valor.id) == str(id):
                return atual.valor
            atual = atual.proximo

        return None

    def buscarNomeProduto(self, nomeProduto):
        atual = self.head
        nome = nome.lower()

        while atual is not None:
            if atual.valor.nome.lower() == nome:
                return atual.valor
            atual = atual.proximo

        return None

        def buscarNomeCliente(self, nomeCliente):
        atual = self.head
        nome = nome.lower()

        while atual is not None:
            if atual.valor.nome.lower() == nome:
                return atual.valor
            atual = atual.proximo

        return None
        
    def removerIdProduto(self, idProduto):
        atual = self.head
        anterior = None

        while atual is not None:
            if str(atual.valor.id) == str(id):
                if anterior is None:
                    self.head = atual.proximo
                else:
                    anterior.proximo = atual.proximo
                return atual.valor

            anterior = atual
            atual = atual.proximo

        return None

        def removerIdCliente(self, idCliente):
        atual = self.head
        anterior = None

        while atual is not None:
            if str(atual.valor.id) == str(id):
                if anterior is None:
                    self.head = atual.proximo
                else:
                    anterior.proximo = atual.proximo
                return atual.valor

            anterior = atual
            atual = atual.proximo

        return None
        
    def estaVazia(self):
        return self.head is None
