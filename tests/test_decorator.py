
def test_garantia_decorator():
    notebook = Notebook("N1", "Prata", 3500, 8)
    decorado = GarantiaEstendidaDecorator(notebook, 24)
    assert "Garantia Estendida" in decorado.get_info()
    assert "24 meses" in decorado.get_info()

