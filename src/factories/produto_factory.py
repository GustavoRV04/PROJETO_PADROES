from src.models.desktop import Desktop
from src.models.notebook import Notebook

class ProdutoFactory:
    def criar_produto(self, tipo, **kwargs):
        if tipo == "desktop":
            return Desktop(**kwargs)
        elif tipo == "notebook":
            return Notebook(**kwargs)
        else:
            raise ValueError("Tipo de produto inválido.")
