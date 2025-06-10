from src.decorators.produto_decorator import GarantiaEstendidaDecorator
from src.models.desktop import Desktop
from src.models.notebook import Notebook

def test_garantia_decorator():
    notebook = Notebook("N1", "Prata", 3500, 8)
    decorado = GarantiaEstendidaDecorator(notebook, 24)
    assert "Garantia Estendida" in decorado.get_info()
    assert "24 meses" in decorado.get_info()

