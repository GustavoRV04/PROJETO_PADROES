
from src.core.cadastro_manager import CadastroManager
from src.factories.produto_factory import ProdutoFactory

class SistemaFacade:
    def __init__(self):
        self._cadastro = CadastroManager()
        self._factory = ProdutoFactory()

    def cadastrar_produto(self, tipo, **kwargs):
        produto = self._factory.criar_produto(tipo, **kwargs)
        self._cadastro.adicionar_produto(produto)
        return produto

    def adicionar_produto_existente(self, produto):
        self._cadastro.adicionar_produto(produto)
        return produto

    def gerar_relatorio(self):
        produtos = self._cadastro.listar_produtos()
        return {
            'total_produtos': len(produtos),
            'produtos': produtos
        }