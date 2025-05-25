from src.models.produto import Produto

class Desktop(Produto):
    def __init__(self, modelo, cor, preco, potenciaDaFonte):
        super().__init__(modelo, cor, preco)
        self._potenciaDaFonte = potenciaDaFonte

    def get_info(self):
        return super().get_info() + f", Potência da Fonte: {self._potenciaDaFonte}W"
