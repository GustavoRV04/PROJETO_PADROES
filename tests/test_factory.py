import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.factories.produto_factory import ProdutoFactory

def test_criacao_desktop():
    factory = ProdutoFactory()
    produto = factory.criar_produto("desktop", modelo="X1", cor="Preto", preco=2500, potenciaDaFonte=500)
    assert "Potência da Fonte" in produto.get_info()

def test_criacao_notebook():
    factory = ProdutoFactory()
    produto = factory.criar_produto("notebook", modelo="N1", cor="Prata", preco=3500, tempoDeBateria=8)
    assert "Tempo de Bateria" in produto.get_info()
