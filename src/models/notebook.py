from src.models.produto import Produto

class Notebook(Produto):
    def __init__(self, modelo, cor, preco, tempoDeBateria):
        super().__init__(modelo, cor, preco)
        self.__tempoDeBateria = tempoDeBateria

    def get_info(self):
        return super().get_info() + f", Tempo de Bateria: {self.__tempoDeBateria}h"
