
from src.models.produto import Produto

class ProdutoDecorator(Produto):
    def __init__(self, produto):
        self._produto = produto

    def get_info(self):
        return self._produto.get_info()

class GarantiaEstendidaDecorator(ProdutoDecorator):
    def __init__(self, produto, meses_garantia):
        super().__init__(produto)
        self._meses_garantia = meses_garantia

    def get_info(self):
        return f"{super().get_info()}, Garantia Estendida: {self._meses_garantia} meses"