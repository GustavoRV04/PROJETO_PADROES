class Produto:
    def __init__(self, modelo, cor, preco):
        self.modelo = modelo
        self.cor = cor
        self.preco = preco

    def get_info(self):
        return f"Modelo: {self.modelo}, Cor: {self.cor}, Preço: R${self.preco}"
