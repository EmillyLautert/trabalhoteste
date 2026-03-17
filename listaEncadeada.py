class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None


class ListaEncadeada:
    def __init__(self):
        self.head = None

    def inserirFim(self, valor):
        novoNodo = Nodo(valor)

        if self.head is None:
            self.head = novoNodo
            return

        atual = self.head
        while atual.proximo is not None:
            atual = atual.proximo

        atual.proximo = novoNodo

    def listar(self):
        elementos = []
        atual = self.head

        while atual is not None:
            elementos.append(atual.valor)
            atual = atual.proximo

        return elementos

    def buscarClientePorId(self, idCliente):
        atual = self.head

        while atual is not None:
            if hasattr(atual.valor, "idCliente"):
                if str(atual.valor.idCliente) == str(idCliente):
                    return atual.valor
            atual = atual.proximo

        return None

    def buscarClientePorNome(self, nomeCliente):
        atual = self.head
        nomeCliente = nomeCliente.lower()

        while atual is not None:
            if hasattr(atual.valor, "nomeCliente"):
                if atual.valor.nomeCliente.lower() == nomeCliente:
                    return atual.valor
            atual = atual.proximo

        return None

    def buscarProdutoPorId(self, idProduto):
        atual = self.head

        while atual is not None:
            if hasattr(atual.valor, "idProduto"):
                if str(atual.valor.idProduto) == str(idProduto):
                    return atual.valor
            atual = atual.proximo

        return None

    def buscarProdutoPorNome(self, nomeProduto):
        atual = self.head
        nomeProduto = nomeProduto.lower()

        while atual is not None:
            if hasattr(atual.valor, "nomeProduto"):
                if atual.valor.nomeProduto.lower() == nomeProduto:
                    return atual.valor
            atual = atual.proximo

        return None

    def removerClientePorId(self, idCliente):
        atual = self.head
        anterior = None

        while atual is not None:
            if hasattr(atual.valor, "idCliente"):
                if str(atual.valor.idCliente) == str(idCliente):
                    if anterior is None:
                        self.head = atual.proximo
                    else:
                        anterior.proximo = atual.proximo
                    return atual.valor

            anterior = atual
            atual = atual.proximo

        return None

    def removerProdutoPorId(self, idProduto):
        atual = self.head
        anterior = None

        while atual is not None:
            if hasattr(atual.valor, "idProduto"):
                if str(atual.valor.idProduto) == str(idProduto):
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
