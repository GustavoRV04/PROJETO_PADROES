
from abc import ABC, abstractmethod

class ProdutoObserver(ABC):
    @abstractmethod
    def atualizar(self, produto):
        pass

class EmailNotificacaoObserver(ProdutoObserver):
    def atualizar(self, produto):
        print(f"Email enviado: O produto {produto.modelo} foi atualizado")

class LogObserver(ProdutoObserver):
    def atualizar(self, produto):
        print(f"Log: Alteração no produto {produto.modelo} registrada")


class Produto:
    def __init__(self, modelo, cor, preco):
        self.modelo = modelo
        self.cor = cor
        self._preco = preco
        self._observers = []

    def adicionar_observer(self, observer):
        self._observers.append(observer)

    def remover_observer(self, observer):
        self._observers.remove(observer)

    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, value):
        self._preco = value
        self._notificar_observers()

    def _notificar_observers(self):
        for observer in self._observers:
            observer.atualizar(self)