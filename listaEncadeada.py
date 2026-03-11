class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None


class ListaEncadeada:
    def __init__(self):
        self.head = None

    def inserir_fim(self, valor):
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

    def buscar_por_id(self, id):
        atual = self.head

        while atual is not None:
            if str(atual.valor.id) == str(id):
                return atual.valor
            atual = atual.proximo

        return None

    def buscar_por_nome(self, nome):
        atual = self.head
        nome = nome.lower()

        while atual is not None:
            if atual.valor.nome.lower() == nome:
                return atual.valor
            atual = atual.proximo

        return None

    def remover_por_id(self, id):
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

    def esta_vazia(self):
        return self.head is None