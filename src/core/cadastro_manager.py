class CadastroManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.produtos = []
        return cls._instance

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def listar_produtos(self):
        return [p.get_info() for p in self.produtos]
